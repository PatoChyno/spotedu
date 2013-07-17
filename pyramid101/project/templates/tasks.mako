<%inherit file="default.mako" />
<%block name="title">Prihlasenie</%block>
<%block name="page_content">
% for task in tasks:
    <div> ${task.task} assigned to ${task.user}
% endfor
</%block>
