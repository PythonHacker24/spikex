#!/usr/share/python3 

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort,json
import json
import os
import re

from attack_engine import get_ip, dir_enum, sub_enum, get_robots, get_sitemap, href_spider, form_spider, http_header_data, http_response

allow_robots_list = []
disallow_robots_list = []
dir_wordlist_location = ""
sub_wordlist_location = ""
form_spider_int_list = []

app = Flask(__name__)
app.secret_key = 'zCyWtCOzMovXOYNxfOoVhSYFpLtbvvNdWGDnxdGeWitbcPRPTx'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/attack_page', methods=['GET', 'POST'])
def scan_results():
    if request.method == 'POST':
        full_url = request.form['target_url']
        domain_name = re.findall('(?:://)(.*)', str(full_url))
        protocol = re.findall('(.*?)(?:://)', str(full_url))

        # initial target scanning
        
        #get_robots(full_url, allow_robots_list, disallow_robots_list)

        #form_spider_int_list[0] = form_spider(full_url)

        # with open('json/target_init/ip_info.json', 'w') as ip_info_json:
        #     json.dump(get_ip(domain_name), ip_info_json)
        # with open('json/target_init/dir_enum.json', 'w') as dir_enum_json:
        #     json.dump(dir_enum(full_url, dir_wordlist_location), dir_enum_json)
        # with open('json/target_init/sub_enum.json', 'w') as sub_enum_json:
        #     json.dump(sub_enum(domain_name, protocol, sub_wordlist_location), sub_enum_json)
        # with open('json/target_init/allow_robots.json', 'w') as allow_robots_json:
        #     json.dump(allow_robots_list, allow_robots_json)
        # with open('json/target_init/disallow_robots.json', 'w') as disallow_robots_json:
        #     json.dump(disallow_robots_list, disallow_robots_json)
        # with open('json/target_init/sitemap.json', 'w') as sitemap_json:
        #     json.dump(get_sitemap(full_url), sitemap_json)
        # with open('json/target_init/href_spider.json', 'w') as href_spider_json:
        #     json.dump(href_spider(full_url), href_spider_json)  
        # with open('json/target_init/form_spider.json', 'w') as form_spider_json:
        #     json.dump(form_spider_int_list, form_spider_json)

        test = http_header_data(full_url)
        with open('json/target_init/http_header_data.json', 'w') as http_header_data_json:
            json.dump(dict(test), http_header_data_json)      
        
        # json_data = open(url_for('static', filename="json/target_init/ip_info.json"))
        # ip_info_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/dir_enum.json"))
        # dir_enum_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/sub_enum.json"))
        # sub_enum_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/allow_robots.json"))
        # allow_robots_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/disallow_robots.json"))
        # disallow_robots_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/sitemap.json"))
        # sitemap_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/href_spider.json"))
        # href_spider_pass = json.load(json_data)

        # json_data = open(url_for('static', filename="json/target_init/form_spider.json"))
        # form_spider_pass = json.load(json_data)

        json_data = open(url_for('static', filename="json/target_init/http_header_data.json"))
        http_header_data_pass = json.load(json_data)

        return render_template('attack_page.html', ip_info_pass=ip_info_pass, dir_enum_pass=dir_enum_pass, sub_enum_pass=sub_enum_pass, allow_robots_pass=allow_robots_pass, disallow_robots_pass=disallow_robots_pass, sitemap_pass=sitemap_pass, href_spider_pass=href_spider_pass, form_spider_pass=form_spider_pass, http_header_data_pass=http_header_data_pass)
