import rangetable_data as data

stamp = [ '1361483964', 'Thu Feb 21 22:59:24 CET 2013', '1.13']

guns = {
    'M224 60mm mortar':[ 'M224','60mm mortar',
        [
        'HE', [ 'Impact Fuze', 'Proximity Burst', 'Near-Surface Burst' ],
            data.m224_60mm_HE_Charge0,
            data.m224_60mm_HE_Charge1,
            data.m224_60mm_HE_Charge2,
            data.m224_60mm_HE_Charge3,
            data.m224_60mm_HE_Charge4
        ],
        [
        'WP', [ 'Impact Fuze', 'Proximity Burst', 'Near-Surface Burst' ],
            data.m224_60mm_WP_Charge0,
            data.m224_60mm_WP_Charge1,
            data.m224_60mm_WP_Charge2,
            data.m224_60mm_WP_Charge3,
            data.m224_60mm_WP_Charge4
        ],
        [
        'Illum', [ 'Time fuze' ],
            data.m224_60mm_Illum_Charge1,
            data.m224_60mm_Illum_Charge2,
            data.m224_60mm_Illum_Charge3,
            data.m224_60mm_Illum_Charge4
        ]

    ],
    'M252 81mm mortar':[ 'M252','81mm mortar',
        [
        'HE', [ 'Impact Fuze', 'Proximity Burst', 'Near-Surface Burst' ],
            data.m252_81mm_HE_Charge0,
            data.m252_81mm_HE_Charge1,
            data.m252_81mm_HE_Charge2,
            data.m252_81mm_HE_Charge3,
            data.m252_81mm_HE_Charge4
        ],
        [
        'WP', [ 'Impact Fuze', 'Proximity Burst', 'Near-Surface Burst' ],
            data.m252_81mm_WP_Charge0,
            data.m252_81mm_WP_Charge1,
            data.m252_81mm_WP_Charge2,
            data.m252_81mm_WP_Charge3,
            data.m252_81mm_WP_Charge4
        ],
        [
        'Illum', [ 'Time fuze' ],
            data.m252_81mm_Illum_Charge1,
            data.m252_81mm_Illum_Charge2,
            data.m252_81mm_Illum_Charge3,
            data.m252_81mm_Illum_Charge4
        ]
    ]
}
