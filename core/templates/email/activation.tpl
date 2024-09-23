{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{user.name}}
{% endblock %}

{% block body %}
{{token}}
{% endblock %}

{% block html %}
{{token}}
{% endblock %}