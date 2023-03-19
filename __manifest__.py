{
    'name': 'Most View And Sold Products ',
    'version': '16.0.1.0.0',
    'sequence': '-1',

    'depends': ['base', 'sale', 'website'],
    'data': [
        'views/most_sold_viewed.xml',
        'views/snippet_most_sold_viewed.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'most_sold_viewed/static/src/js/most_sold_viewed.js',
            'most_sold_viewed/static/src/xml/template_most_sold_viewed.xml',
            'most_sold_viewed/static/src/css/most_sold_viewed.scss'
        ]
    }
}
