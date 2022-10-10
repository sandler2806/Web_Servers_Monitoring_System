from WebServersMonitoring import WebServersMonitoring

def insert_urls():
    urls = ['http://webcode.me', 'https://httpbin.org/get',
            'https://google.com', 'https://stackoverflow.com',
            'https://github.com', 'https://clojure.org',
            'https://fsharp.org']

    for i, url in enumerate(urls):
        WebServersMonitoring.create_webserver(chr(ord('a') + i), url)
        WebServersMonitoring.request(chr(ord('a') + i), 'success')


if __name__ == '__main__':
    # create tables
    WebServersMonitoring.create_tables()

    # insert urls
    insert_urls()
    print(WebServersMonitoring.get_all())
    print(WebServersMonitoring.get('a'))
    print(WebServersMonitoring.get('b'))

    # delete a and b
    WebServersMonitoring.delete_webserver('b')
    WebServersMonitoring.delete_webserver('a')

    # check that a and b deleted
    print(WebServersMonitoring.get_all())
    print(WebServersMonitoring.read_webserver('b'))
    print(WebServersMonitoring.get('b'))
    print(WebServersMonitoring.read_webserver('a'))
    print(WebServersMonitoring.get('a'))

    # create a again
    WebServersMonitoring.create_webserver(chr(ord('a')), 'http://webcode.me')
    WebServersMonitoring.request('a', 'success')
    # check a exist
    print(WebServersMonitoring.get_all())
    print(WebServersMonitoring.read_webserver('a'))
    print(WebServersMonitoring.get('a'))

    # update a to b
    WebServersMonitoring.update_webserver(old_name='a', new_name='b')
    print(WebServersMonitoring.get_all())
    print(WebServersMonitoring.read_webserver('b'))

    # update the url
    WebServersMonitoring.update_webserver(old_name='b', new_url='https://httpbin.org/get')
    print(WebServersMonitoring.get_all())
    print(WebServersMonitoring.read_webserver('b'))
