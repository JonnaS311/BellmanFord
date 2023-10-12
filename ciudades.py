ciudades = [
    {
        "name":"bog",
        "id": 0,
        "ciudades_adyacentes":{"per":10,"tun":7, "vil":12},
        "distancia_destino":100
    },
    {
        "name":"tun",
        "id": 1,
        "ciudades_adyacentes":{"bog":7,"yop":5, "buc":11},
        "distancia_destino":91
    },
    {
        "name":"yop",
        "id": 2,
        "ciudades_adyacentes":{"tun":5},
        "distancia_destino":120
    },
    {
        "name":"buc",
        "id": 3,
        "ciudades_adyacentes":{"tun":11,"cuc":15, "val":20},
        "distancia_destino":80
    },
    {
        "name":"cuc",
        "id": 4,
        "ciudades_adyacentes":{"buc":15},
        "distancia_destino":110
    },
    {
        "name":"val",
        "id": 5,
        "ciudades_adyacentes":{"buc":20,"san":8, "bar":20},
        "distancia_destino":50
    },
    {
        "name":"san",
        "id": 6,
        "ciudades_adyacentes":{"val":8,"rio":15, "bar":11},
        "distancia_destino":43
    },
    {
        "name":"rio",
        "id": 7,
        "ciudades_adyacentes":{"san":15},
        "distancia_destino":75
    },
    {
        "name":"bar",
        "id": 8,
        "ciudades_adyacentes":{"san":11,"val":20, "car":6},
        "distancia_destino":18
    },
    {
        "name":"car",
        "id": 9,
        "ciudades_adyacentes":{"bar":6,"sin":13},
        "distancia_destino":0
    },
    {
        "name":"sin",
        "id": 10,
        "ciudades_adyacentes":{"car":13,"med":16},
        "distancia_destino":25
    },
    {
        "name":"med",
        "id": 11,
        "ciudades_adyacentes":{"man":8,"per":8, "cal":13, "pas":25, "sin":16},
        "distancia_destino":41
    },
    {
        "name":"man",
        "id": 12,
        "ciudades_adyacentes":{"med":8,"per":4},
        "distancia_destino":52
    },
    {
        "name":"per",
        "id": 13,
        "ciudades_adyacentes":{"med":8,"man":4,"cal":12,"bog":10}, #faltaba cali
        "distancia_destino":63
    },
    {
        "name":"cal",
        "id": 14,
        "ciudades_adyacentes":{"per":12,"med":13, "pop":8},
        "distancia_destino":77
    },
    {
        "name":"pop",
        "id": 15,
        "ciudades_adyacentes":{"cal":8,"nei":15, "pas":10},
        "distancia_destino":88
    },
    {
        "name":"pas",
        "id": 16,
        "ciudades_adyacentes":{"pop":10,"med":25},
        "distancia_destino":121
    },
    {
        "name":"nei",
        "id": 17,
        "ciudades_adyacentes":{"pop":15,"let":20},
        "distancia_destino":130
    },
    {
        "name":"let",
        "id": 18,
        "ciudades_adyacentes":{"nev":20,"vil":26},
        "distancia_destino":200
    },
    {
        "name":"vil",
        "id": 19,
        "ciudades_adyacentes":{"bog":12,"let":26},
        "distancia_destino":118
    }
]

