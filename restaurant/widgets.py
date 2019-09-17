from django import forms


class LocationWidget(forms.TextInput):
    template_name = 'widgets/location_widget.html'

    class Media:
        js = [
            '//maps.googleapis.com/maps/api/js', # FIXME: Google Maps JavaScript API 키 적용
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['readonly'] = True
        attrs['style'] = 'background-color: #eee; border: 0;'
        return attrs