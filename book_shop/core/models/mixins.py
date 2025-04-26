class AutoTemplateMixin:

    class Meta:
        abstract = True

    def get_template_names(self):
        return [
            f'{self.model._meta.app_label}/'
            f'{self.model._meta.model_name}'
            f'{self.template_name_suffix}.html'
        ]
