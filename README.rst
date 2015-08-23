Django materialize form
=======================

A simple Django library to render your form in `Material Design <http://materializecss.com/>`_

Installation
------------
::

    pip install django-materialize-form

Usage
-----

* Add **"materializeform"** to your INSTALLED_APPS.

* At the top of your django templates load our templatetags
  ::

    {% load materialize %}

Then to render your form
------------------------
::

    <form action='.' method='post'>
        {% csrf_token %}
        {{ form|materialize }}
        <button type='submit' class="btn blue">Submit</button>
    </form>

You can also set column class for each fields on the form
---------------------------------------------------------
::

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

If you have 'select' menu in your form
--------------------------------------
Then please include,
::

    <script>
      $(function(){
        $(document).ready(function() {
          $('select.select').material_select();
          $('select.multiselect').show();
        });
      });
    </script>
