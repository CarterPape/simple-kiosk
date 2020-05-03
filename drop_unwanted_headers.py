import mitmproxy

def response(flow: mitmproxy.http.HTTPFlow) -> None:
    if "X-Frame-Options" in flow.response.headers:
        flow.response.headers.pop("X-Frame-Options")
