from rest_framework import permissions

class ModelPermissions(permissions.BasePermission):
    """
    Grants permissions based on Django model permissions dynamically.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Map DRF actions to Django's built-in permissions
        perms_map = {
            "create": "add",
            "list": "view",
            "retrieve": "view",
            "update": "change",
            "partial_update": "change",
            "destroy": "delete",
        }

        action = view.action
        model_name = view.queryset.model._meta.model_name  # Dynamically get model name
        app_label = view.queryset.model._meta.app_label  # Get app name

        # Get the corresponding Django permission (e.g., "app.view_model")
        perm = f"{app_label}.{perms_map.get(action, '')}_{model_name}"

        return request.user.has_perm(perm)