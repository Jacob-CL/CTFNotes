# cURL
## Cheatsheet
- https://devhints.io/curl

## Examples

## Notes
- Basic usage: `curl google.com`
- Output result to a file: `curl -O inlanefreight.com/index.html`
- Skip the certificate check: `curl -k https://inlanefreight.com`
- See both request and response: `curl inlanefreight.com -v` (or `-vvv` for even more verbosity)
- Only want to see headers?: `curl -I https://example.com`
- to include HTTP response headers use `-i`
- `-A` to set the User-Agent
