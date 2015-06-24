from django import forms
from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()


def render(element, markup_classes):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template("materializeform/field.html")
        context = Context({'field': element, 'classes': markup_classes, 'form': element.form})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template("materializeform/formset.html")
            context = Context({'formset': element, 'classes': markup_classes})
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template("materializeform/form.html")
            context = Context({'form': element, 'classes': markup_classes})

    return template.render(context)


@register.filter
def add_input_classes(field):
    if not is_checkbox(field) and not is_multiple_checkbox(field) and not is_radio(field) and not is_file(field):
        field_classes = [field.field.widget.attrs.get('class', ''), 'validate']
        if is_textarea(field):
            field_classes.append('materialize-textarea')
        elif is_select(field):
            if not is_multi_select(field):
                field_classes.append('select')
            else:
                field_classes.append('multiselect')
        if field.errors:
            field_classes.append('invalid')
        field.field.widget.attrs['class'] = " ".join(field_classes)


@register.filter
def materialize(element, col="s12"):
    markup_classes = {'col': col}
    return render(element, markup_classes)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_select(field):
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_multi_select(field):
    return isinstance(field.field.widget, forms.SelectMultiple)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_textarea(field):
    return isinstance(field.field.widget, forms.Textarea)
