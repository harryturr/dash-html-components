# AUTO GENERATED FILE - DO NOT EDIT

export html_img

"""
    html_img(;kwargs...)
    html_img(children::Any;kwargs...)
    html_img(children_maker::Function;kwargs...)


An Img component.
Img is a wrapper for the <img> HTML5 element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `accessKey` (String; optional): Keyboard shortcut to activate or add focus to the element.
- `alt` (String; optional): Alternative text in case an image can't be displayed.
- `aria-*` (String; optional): A wildcard aria attribute
- `className` (String; optional): Often used with CSS to style elements with common properties.
- `contentEditable` (String; optional): Indicates whether the element's content is editable.
- `contextMenu` (String; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- `crossOrigin` (String; optional): How the element handles cross-origin requests
- `data-*` (String; optional): A wildcard data attribute
- `dir` (String; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- `draggable` (String; optional): Defines whether the element can be dragged.
- `height` (String | Real; optional): Specifies the height of elements listed here. For all other elements, use the CSS height property.        Note: In some instances, such as <div>, this is a legacy attribute, in which case the CSS height property should be used instead.
- `hidden` (a value equal to: 'hidden', 'HIDDEN' | Bool; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- `key` (String; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- `lang` (String; optional): Defines the language used in the element.
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `n_clicks` (Real; optional): An integer that represents the number of times
that this element has been clicked on.
- `n_clicks_timestamp` (Real; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- `referrerPolicy` (String; optional): Specifies which referrer is sent when fetching the resource.
- `role` (String; optional): The ARIA role attribute
- `sizes` (String; optional)
- `spellCheck` (String; optional): Indicates whether spell checking is allowed for the element.
- `src` (String; optional): The URL of the embeddable content.
- `srcSet` (String; optional): One or more responsive image candidates.
- `style` (Dict; optional): Defines CSS styles which will override styles previously set.
- `tabIndex` (String; optional): Overrides the browser's default tab order and follows the one specified instead.
- `title` (String; optional): Text to be displayed in a tooltip when hovering over the element.
- `useMap` (String; optional)
- `width` (String | Real; optional): For the elements listed here, this establishes the element's width.        Note: For all other instances, such as <div>, this is a legacy attribute, in which case the CSS width property should be used instead.
"""
function html_img(; kwargs...)
        available_props = Symbol[:children, :id, :accessKey, :alt, :className, :contentEditable, :contextMenu, :crossOrigin, :dir, :draggable, :height, :hidden, :key, :lang, :loading_state, :n_clicks, :n_clicks_timestamp, :referrerPolicy, :role, :sizes, :spellCheck, :src, :srcSet, :style, :tabIndex, :title, :useMap, :width]
        wild_props = Symbol[Symbol("aria-"), Symbol("data-")]
        return Component("html_img", "Img", "dash_html_components", available_props, wild_props; kwargs...)
end

html_img(children::Any; kwargs...) = html_img(;kwargs..., children = children)
html_img(children_maker::Function; kwargs...) = html_img(children_maker(); kwargs...)
