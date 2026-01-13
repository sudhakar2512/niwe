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



# myapp/middleware.py

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

class SessionSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:

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

                  # Get the 'is_private_mode' cookie set by JavaScript
            is_private_mode = request.COOKIES.get('is_private_mode', 'false')

        # Check if the session already has the 'login_mode' value
            session_mode = request.session.get('login_mode')

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

        # If the session mode doesn't match the expected mode (cookie value)
            if session_mode != ('private' if is_private_mode == 'true' else 'normal'):
                # Invalidate the session to prevent session fixation
                logout(request)
                return HttpResponseRedirect('/admin/login/')


        return self.get_response(request)

