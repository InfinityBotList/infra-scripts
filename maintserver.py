import fastapi
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi import status, HTTPException

app = fastapi.FastAPI(openapi_url=None)

hosts = {
    "infinitybots.gg": "https://discord.gg/cRuprw9CGz",
    "jobcord.co": "https://discord.gg/E3tan4FRux",
    "reviewbots.xyz": "https://discord.gg/azdFD5fG6j",
    "diswidgets.org": "https://discord.gg/ar65ACHcVd",
    "chillcord.life": "https://discord.gg/cRuprw9CGz",
    "select-list.xyz": "https://discord.gg/XdGs8WFFtK",
}

status_pages = {
    "select-list.xyz": "https://status.select-list.xyz/"
}


@app.get("/{route:path}")
@app.post("/{route:path}")
@app.delete("/{route:path}")
@app.put("/{route:path}")
@app.patch("/{route:path}")
@app.head("/{route:path}")
@app.options("/{route:path}")
def path(request: fastapi.Request):
    inv = "#error"
    status_iframe = ""
    for host, invite in hosts.items():
        print(host, str(request.url), request.url.hostname)
        if request.url.hostname.endswith(host):
            inv = invite
            if status_pages.get(host):
                status_iframe = f'<iframe src="{status_pages[host]}" />'

    if str(request.url).startswith("https://api.") or str(request.url).startswith("https://metro."):
        return ORJSONResponse({"detail": "Down for maintenance", "invite": inv}, status_code=408)

    css = """
     h1, h2, h3, h4, a, p, small, ol, li, details, summary {
        font-family: 'Montserrat', sans-serif;
        color: white;
        font-weight: bold;
     }

     code {
         font-weight: normal;
     }

     a {
        text-decoration: none;
        border-radius: 5px 5px 5px 5px;
        border: 1px solid #7289DA;
        background-color: #23272a;
        padding: 10px;
     }

     code {
      background-color: #23272a;
      text-color: #7289da;
     }

     body {
            background: linear-gradient(175deg,#1410B4,#250937) !important;
            overflow-x: hidden !important;
            background: #16151d!important;
            background-color: #16151d!important;
            background-image: url('https://media.discordapp.net/attachments/653733403841134600/982486269730893844/06A86F34-55B7-40E3-B762-745877C89844.png') !important;
            background-size: cover !important;
            background-repeat: no-repeat !important;
            background-position: center center !important;
            background-attachment: fixed !important;
            background-blend-mode: overlay !important;
        }
        .box{
          width: 100%;
          background-color: #23272a;
          border: 1px solid #7289DA;
          word-wrap: break-word;
        }
        .footer {
          position: fixed;
          left: 0;
          bottom: 0;
          width: 100%;
          border: 1px solid #7289DA;
          background-color: #23272a;
          color: white;
          text-align: center;
        }
        h1, h2, h3, h4, a, p {
            color: white;
        }
    """

    return HTMLResponse(f"""
<html>
    <head>
        <title>503 - Maintenance</title>
         <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="../../www.w3schools.com/w3css/4/w3.css">
          <script src="https://kit.fontawesome.com/22859885a2.js" crossorigin="anonymous"></script>
          <link rel="preconnect" href="https://fonts.googleapis.com">
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@1,600&display=swap" rel="stylesheet">
        <style>
            {css}
        </style>
    </head>
    <body>
      <center>
      <br /><br />
        <h1>Error: 503</h1>
        <h2>Service Temporarily Unavailable</h2>
         <a type="button" class="btn btn-primary" href="{inv}"><i class="fab fa-discord"></i> Support Server</a>
         <a type="button" class="btn btn-secondary" href="https://{request.url.hostname}" disabled><i class="fas fa-globe"></i> Visit Website</a>
         <br /><br />
        <hr />
        <h3>Whoops, looks like the service is currently unable to handle requests or down for maintenance!</h3>
        <h3>You can use the button(s) above to join the support server for this service and find out more info.</h3>
        <br /><br />
        <h3><i class="fa fa-exclamation-circle"></i> <strong>NOTE:</strong> This page will return a JSON friendly status code of <code>408</code> this should be respected in all modules/librarys</h3>
        <hr />
        {status_iframe}
         <details open>
            <summary>Scope & Request Info</summary>
            <br />
            <div class="box">
               <br /><br />
                 <code>{str(request.scope).replace("<", "&lt").replace(">", "&gt")}</code>
               <br /><br />
            </div>
        </details>
      </center>
    </body>
</html>
    """, status_code=408)
