'''
Module for all the styles used in the project
'''
table_styles= {
    'indigo_palette' : [
        dict(selector="th", props=[("color", "#FFFFFF"), ("background", "#283593"), ("text-transform", "capitalize")]),
        dict(selector="td", props=[("color", "#333333")]),
        dict(selector="table", props=[("font-family", 'Arial'), ("border-collapse", "collapse")]),
        dict(selector='tr:nth-child(even)', props=[('background', '#E8EAF6')]),
        dict(selector='tr:nth-child(odd)', props=[('background', '#FFFFFF')]),
        dict(selector="th", props=[("border", "1px solid #5C6BC0")]),
        dict(selector="td", props=[("border", "1px solid #5C6BC0")]),
        dict(selector="tr:hover", props=[("background", "#9FA8DA")])
    ],
    'cerulean_palette' : [
        dict(selector="th", props=[("color", "#FFFFFF"), ("background", "#004D80"), ("text-transform", "capitalize")]),
        dict(selector="td", props=[("color", "#333333")]),
        dict(selector="table", props=[("font-family", 'Arial'), ("border-collapse", "collapse")]),
        dict(selector='tr:nth-child(even)', props=[('background', '#D3EEFF')]),
        dict(selector='tr:nth-child(odd)', props=[('background', '#FFFFFF')]),
        dict(selector="th", props=[("border", "1px solid #0070BA")]),
        dict(selector="td", props=[("border", "1px solid #0070BA")]),
        dict(selector="tr:hover", props=[("background", "#80D0FF")])
    ],
    'denim_palette' : [
        dict(selector="th", props=[("color", "#FFFFFF"), ("background", "#1C4966"), ("text-transform", "capitalize")]),
        dict(selector="td", props=[("color", "#333333")]),
        dict(selector="table", props=[("font-family", 'Arial'), ("border-collapse", "collapse")]),
        dict(selector='tr:nth-child(even)', props=[('background', '#C9E7F4')]),
        dict(selector='tr:nth-child(odd)', props=[('background', '#FFFFFF')]),
        dict(selector="th", props=[("border", "1px solid #3A89C9")]),
        dict(selector="td", props=[("border", "1px solid #3A89C9")]),
        dict(selector="tr:hover", props=[("background", "#77B5D9")])
    ],
    'cobalt_palette' : [
        dict(selector="th", props=[("color", "#FFFFFF"), ("background", "#0042A1"), ("text-transform", "capitalize")]),
        dict(selector="td", props=[("color", "#333333")]),
        dict(selector="table", props=[("font-family", 'Arial'), ("border-collapse", "collapse")]),
        dict(selector='tr:nth-child(even)', props=[('background', '#D9E8FF')]),
        dict(selector='tr:nth-child(odd)', props=[('background', '#FFFFFF')]),
        dict(selector="th", props=[("border", "1px solid #1C7ED6")]),
        dict(selector="td", props=[("border", "1px solid #1C7ED6")]),
        dict(selector="tr:hover", props=[("background", "#6AAAFF")])
    ]
}
