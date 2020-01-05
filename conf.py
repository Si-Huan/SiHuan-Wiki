# -*- coding: utf-8 -*-
"""SiHuan维基构建配置文件
"""

# For Maverick
site_prefix = "/"
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/Si-Huan/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "Si-Huan/SiHuan-Blog@gh-pages"
}

# 站点设置
site_name = "SiHuan's Wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-01T00:00+08:00"
author = "SiHuan"
email = "sihuan@sakuya.love"
author_homepage = "https://www.sakuya.love"
description = "道阻且长，君子思还。"
key_words = ['SiHuan', '思还', 'Wiki', '维基', 'GitWiki']
language = 'zh-CN'
external_links = [
    {
        "name": "SiHuan-Blog
        "url": "http://blog.sakuya.love",
        "brief": "我的博客。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Telegram",
        "url": "https://t.me/Si_Huan",
        "icon": "gi gi-telegram"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Si-Huan",
        "icon": "gi gi-github"
    }
    # ,
    # {
    #     "name": "QQ",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-twitter"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
