import logging
from datetime import timedelta
from django.utils.timezone import now
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime

logger = logging.getLogger(__name__)

class AdminIdleTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply to Django admin paths
        if request.path.startswith(reverse('admin:index')) or request.path.startswith('/admin/'):
            last_activity_str = request.session.get('last_admin_activity')
            timeout = getattr(settings, 'ADMIN_SESSION_IDLE_TIMEOUT', 1200)  # 20 minutes default

            # Convert last_activity_str back to datetime if it exists
            last_activity = None
            if last_activity_str:
                try:
                    last_activity = datetime.fromisoformat(last_activity_str)
                except ValueError:
                    pass  # If conversion fails, ignore it
            

            # Check if the session is idle
            if last_activity and now() - last_activity > timedelta(seconds=timeout):               
                request.session.flush()  # Log out the user
                return redirect(f"{reverse('admin:login')}?next={request.path}")  # Redirect to admin login

            # Update last activity time in ISO format (string)
            request.session['last_admin_activity'] = now().isoformat()

        response = self.get_response(request)
        return response

        



from django.http import HttpResponseRedirect
from django.contrib.auth import logout

import logging
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout

# # Configure logger
# logger = logging.getLogger(__name__)

class SessionSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if request.user.is_authenticated:

            # response = self.get_response(request)
            #request.session.flush() # Clear existing session data
            #request.session.cycle_key()  # Generates a new session key
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT')

            # Bind IP and User-Agent to the session
            if 'ip_address' not in request.session:
                request.session['ip_address'] = ip_address
            if 'user_agent' not in request.session:
                request.session['user_agent'] = user_agent

            # Check if current IP/UA matches stored session values
            if request.session['ip_address'] != ip_address or request.session['user_agent'] != user_agent:
                logout(request)
                return HttpResponseRedirect('/admin/login/')  # Redirect to login

          

             # Check if the user is logged in and if session key should be rotated
            if request.user.is_authenticated and 'sessionid' in request.COOKIES:
            # Check if session key is unchanged since the login
                if 'last_login' not in request.session or request.session.get('last_login') != str(request.user.last_login):
                    request.session.cycle_key()  # Rotate the session key
                    request.session['last_login'] = str(request.user.last_login)  # Store the last login time
                    # Force logout after session rotation (optional)
                    #logout(request) 
                    #return HttpResponseRedirect('/admin/login/')  # Redirect to login




            # Get the 'is_private_mode' cookie set by JavaScript
            is_private_mode = request.COOKIES.get('is_private_mode', 'false')

            # Check if the session already has the 'login_mode' value
            session_mode = request.session.get('login_mode')
            print(is_private_mode)
            
            
            # If session mode is not set, initialize it with the current mode (private or normal)
            if not session_mode:
                if is_private_mode == 'true':
                    request.session['login_mode'] = 'private'
                else:
                    request.session['login_mode'] = 'normal'
        
            # Check if the session already has the 'login_mode' value
            session_mode = request.session.get('login_mode')
            print(session_mode)
           #session_mode = request.session.get('login_mode')
            
             # Log the session values instead of print
            # logger.info("---------------------------------------------------")
            # logger.info(f"Session_mode: {session_mode}")
            # logger.info(f"is_private_mode: {is_private_mode}")

            # If the session mode doesn't match the expected mode (cookie value)
            if session_mode != ('private' if is_private_mode == 'true' else 'normal'):
                # Invalidate the session to prevent session fixation
               
                logout(request)
                return HttpResponseRedirect('/admin/login/')


        return self.get_response(request)


from django.http import HttpResponseForbidden

class BlockBotsMiddleware:
    # List of bot User-Agents to block
    BLOCKED_USER_AGENTS = [
        'Amazonbot',
        'Googlebot',
        'Bingbot',
        'Slurp',  # Yahoo bot
        'DuckDuckBot',
        'YandexBot',
        'Baiduspider',
        # Add more bot user agents as needed
    ]

    # Optionally, you can block specific IPs
    BLOCKED_IPS = [
        '34.196.237.236',  # Example IP from your log
        '203.0.113.0',  # Add more IPs as needed
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check the User-Agent header
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if any(bot in user_agent for bot in self.BLOCKED_USER_AGENTS):
            return HttpResponseForbidden('Access Denied: Bot detected')

        # Optionally, check the client's IP address
        client_ip = request.META.get('REMOTE_ADDR')
        if client_ip in self.BLOCKED_IPS:
            return HttpResponseForbidden('Access Denied: Blocked IP')

        # If the request passes, process it
        response = self.get_response(request)
        return response



