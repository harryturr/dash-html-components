"""
Autogenerated file
DO NOT EDIT.
CONTENT WILL BE OVERWRITTEN!

WARNING: Do not import this file directly!
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class Table(DashComponent):
    """
    
    """
    _namespace = 'dash_html_components'
    _typename = 'Table'
    available_wildcard_properties = [
        'data-',
        'aria-'
    ]
    id = ComponentProp('id', UNDEFINED, False)
    children = ComponentProp('children', UNDEFINED, False)
    n_clicks = ComponentProp('n_clicks', 0, False)
    n_clicks_timestamp = ComponentProp('n_clicks_timestamp', -1, False)
    key = ComponentProp('key', UNDEFINED, False)
    role = ComponentProp('role', UNDEFINED, False)
    summary = ComponentProp('summary', UNDEFINED, False)
    accessKey = ComponentProp('accessKey', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    contentEditable = ComponentProp('contentEditable', UNDEFINED, False)
    contextMenu = ComponentProp('contextMenu', UNDEFINED, False)
    dir = ComponentProp('dir', UNDEFINED, False)
    draggable = ComponentProp('draggable', UNDEFINED, False)
    hidden = ComponentProp('hidden', UNDEFINED, False)
    lang = ComponentProp('lang', UNDEFINED, False)
    spellCheck = ComponentProp('spellCheck', UNDEFINED, False)
    style = ComponentProp('style', UNDEFINED, False)
    tabIndex = ComponentProp('tabIndex', UNDEFINED, False)
    title = ComponentProp('title', UNDEFINED, False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        children=UNDEFINED,
        id=UNDEFINED,
        n_clicks=0,
        n_clicks_timestamp=-1,
        key=UNDEFINED,
        role=UNDEFINED,
        summary=UNDEFINED,
        accessKey=UNDEFINED,
        className=UNDEFINED,
        contentEditable=UNDEFINED,
        contextMenu=UNDEFINED,
        dir=UNDEFINED,
        draggable=UNDEFINED,
        hidden=UNDEFINED,
        lang=UNDEFINED,
        spellCheck=UNDEFINED,
        style=UNDEFINED,
        tabIndex=UNDEFINED,
        title=UNDEFINED,
        loading_state=UNDEFINED,
        **kwargs
    ):
        # type: (typing.Union[typing.Union[str, int, float, DashComponent,typing.List[typing.Union[str, int, float, DashComponent]]], Undefined], typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id: The ID of this component, used to identify dash
            components in callbacks. The ID needs to be unique
            across all of the components in an app.
        :param children: The children of this component
        :param n_clicks: An integer that represents the number of times
            that this element has been clicked on.
        :param n_clicks_timestamp: An integer that represents the time (in
            ms since 1970) at which n_clicks
            changed. This can be used to tell which
            button was changed most recently.
        :param key: A unique identifier for the component, used to improve
            performance by React.js while rendering components See
            https://reactjs.org/docs/lists-and-keys.html for more
            info
        :param role: The ARIA role attribute
        :param summary:
        :param accessKey: Defines a keyboard shortcut to activate or add
            focus to the element.
        :param className: Often used with CSS to style elements with common
            properties.
        :param contentEditable: Indicates whether the element's content is
            editable.
        :param contextMenu: Defines the ID of a <menu> element which will
            serve as the element's context menu.
        :param dir: Defines the text direction. Allowed values are ltr
            (Left-To-Right) or rtl (Right-To-Left)
        :param draggable: Defines whether the element can be dragged.
        :param hidden: Prevents rendering of given element, while keeping
            child elements, e.g. script elements, active.
        :param lang: Defines the language used in the element.
        :param spellCheck: Indicates whether spell checking is allowed for
            the element.
        :param style: Defines CSS styles which will override styles
            previously set.
        :param tabIndex: Overrides the browser's default tab order and
            follows the one specified instead.
        :param title: Text to be displayed in a tooltip when hovering over
            the element.
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
