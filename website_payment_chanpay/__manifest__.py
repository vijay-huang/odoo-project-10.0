# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': "畅捷支付网站端",

    'summary': """
        畅捷支付_website
        
        """,

    'description': """
         1、订单号一维码
        2、畅捷推送支付结果
        3、响应请求并处理
    """,

    'author': 'Gavin Gu',
    'website': '',
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

    # always loaded
    'data': [
        'views/payment_views.xml',
        'views/payment_alipay_templates.xml',
        'views/account_config_settings_views.xml',
        'demo/payment_acquirer_data.xml',
    ],

    "external_dependencies": {
        "python": ['Crypto'],
    },
    # only loaded in demonstration mode
    'installable': True,
    'active': False,
    'application': False,
}
