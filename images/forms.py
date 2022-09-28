from django import forms

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """Return the Image Create Form."""

    class Meta:
        """Display only title, url and description, hide the url field."""

        model = Image
        fields = ["title", "url", "description"]
        widgets = {
            "url": forms.HiddenInput,
        }

    def clean_url(self):
        """Check if URL is valid image file."""
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extensions = url.split(".", 1)[1].lower()
        if extensions not in valid_extensions:
            raise forms.ValidationError(
                "The given URL does not  match valid image extensions."
            )

        return url
