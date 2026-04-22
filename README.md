````markdown
# Service Discovery Script

A simple Python tool for basic service discovery on specific hosts and ports using raw TCP sockets and HTTP requests.

Useful for:

- Identifying active web services
- Checking responses on non-standard ports
- Testing virtual hosts using different `Host` headers
- Basic reconnaissance during internal assessments

---

## Requirements

- Python 3.x

No external dependencies required.

---

## Usage

```bash
python service_discovery.py <ip> --ports <ports> --hosts <hosts>
````

---

## Arguments

| Argument  | Description                                                 |
| --------- | ----------------------------------------------------------- |
| `ip`      | Target IP address                                           |
| `--ports` | Comma-separated list of ports                               |
| `--hosts` | Comma-separated list of hostnames for `Host` header testing |

---

## Examples

### Scan port 80

```bash
python service_discovery.py 192.168.1.10 --ports 80
```

### Scan multiple ports

```bash
python service_discovery.py 192.168.1.10 --ports 80,8080,8000
```

### Test virtual hosts

```bash
python service_discovery.py 192.168.1.10 --ports 80 --hosts example.local,admin.local,test.local
```

---

## How It Works

For each specified port, the script:

1. Opens a TCP connection
2. Sends basic HTTP requests
3. Optionally tests custom `Host` headers
4. Reads and prints the server response

---

## Notes

The script currently uses a fixed socket timeout of 5 seconds.

You may want to extend it with:

* HTTPS support
* Multithreading
* Output to file
* CIDR/range scanning
* Banner grabbing

---

## Disclaimer

Use only on systems you own or are authorized to test.

```
```
