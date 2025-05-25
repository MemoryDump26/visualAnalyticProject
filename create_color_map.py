import hsluv

color_map = {
    "20A.EU2": "rgba(0, 0, 0, 0.5)",
    "20A/S:126A": "rgba(0, 0, 0, 0.5)",
    "20A/S:439K": "rgba(0, 0, 0, 0.5)",
    "20A/S:98F": "rgba(0, 0, 0, 0.5)",
    "20B/S:1122L": "rgba(0, 0, 0, 0.5)",
    "20B/S:626S": "rgba(0, 0, 0, 0.5)",
    "20B/S:732A": "rgba(0, 0, 0, 0.5)",
    "20C/S:80Y": "rgba(0, 0, 0, 0.5)",
    "20E (EU1)": "rgba(0, 0, 0, 0.5)",
    "20H (Beta, V2)": "rgba(0, 0, 0, 0.5)",
    "20I (Alpha, V1)": "rgba(0, 0, 0, 0.5)",
    "20J (Gamma, V3)": "rgba(0, 0, 0, 0.5)",
    "21A (Delta)": "rgba(0, 0, 0, 0.5)",
    "21B (Kappa)": "rgba(0, 0, 0, 0.5)",
    "21C (Epsilon)": "rgba(0, 0, 0, 0.5)",
    "21D (Eta)": "rgba(0, 0, 0, 0.5)",
    "21F (Iota)": "rgba(0, 0, 0, 0.5)",
    "21G (Lambda)": "rgba(0, 0, 0, 0.5)",
    "21H (Mu)": "rgba(0, 0, 0, 0.5)",
    "21I (Delta)": "rgba(0, 0, 0, 0.5)",
    "21J (Delta)": "rgba(0, 0, 0, 0.5)",
    "21K (Omicron)": "rgba(0, 0, 0, 0.5)",
    "21L (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22A (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22B (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22C (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22D (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22E (Omicron)": "rgba(0, 0, 0, 0.5)",
    "22F (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23A (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23B (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23C (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23D (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23E (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23F (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23G (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23H (Omicron)": "rgba(0, 0, 0, 0.5)",
    "23I (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24A (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24B (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24C (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24D (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24E (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24F (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24G (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24H (Omicron)": "rgba(0, 0, 0, 0.5)",
    "24I (Omicron)": "rgba(0, 0, 0, 0.5)",
    "25A (Omicron)": "rgba(0, 0, 0, 0.5)",
    "S:677H.Robin1": "rgba(0, 0, 0, 0.5)",
    "S:677P.Pelican": "rgba(0, 0, 0, 0.5)",
}

special_color = {
    "recombinant": "rgba(10, 10, 10, 0.5)",
    "others": "rgba(150, 150, 150, 0.5)",
}


def create_color_map(opacity=1):
    result = {}
    for idx, variant in enumerate(color_map.keys()):
        hue = (idx / len(color_map.keys())) * 360
        r, g, b = hsluv.hsluv_to_rgb((hue, 70, 70))
        r = round(r * 255)
        g = round(g * 255)
        b = round(b * 255)
        result.update({variant: f"rgba({r}, {g}, {b}, {opacity})"})
        # print(f"rgba({r*255}, {g*255}, {b*255}, 0.5)")
    result.update(special_color)
    return result


if __name__ == "__main__":
    create_color_map()
