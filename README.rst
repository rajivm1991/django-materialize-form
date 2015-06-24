=======================
Django materialize form
=======================

Materialize design for Django Form.

A simple Django template tag to work with `Materialize CSS <http://http://materializecss.com/>`_


Usage
=====

Add "materializeform" to your INSTALLED_APPS.

At the top of your template load in our template tags::

	{% load materialize %}

Then to render your form
------------------------

  <form action='.' method='post'>

    {% csrf_token %}
    {{ form|materialize }}
    
    <button type='submit' class="btn blue">Submit</button>

  </form>

You can also set column class for each fields on the form
---------------------------------------------------------

    <form action='.' method='post'>

        {% csrf_token %}

        <div class="row">
        {{ form.email|materialize:"s12" }}
        </div>

        <div class="row">
        {{ form.first_name|materialize:"s6" }}
        {{ form.last_name|materialize:"s6" }}
        </div>

        <button type='submit' class="btn blue">Submit</button>

    </form>