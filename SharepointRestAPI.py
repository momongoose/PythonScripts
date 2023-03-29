import requests

headers = {
    'Accept': "application/json;odata=verbose",
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImpTMVhvMU9XRGpfNTJ~2YndHTmd2UU8yVnpNYyIsImtpZCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbGlmZWJyYWlubGFib3Iuc2hhcmVwb2ludC5jb21AMzZiY2RlYmYtMWU3YS00YmE4LWFjYzUtNDk2ODFmNjZkMjRmIiwiaXNzIjoiMDAwMDAwMDEtMDAwMC0wMDAwLWMwMDAtMDAwMDAwMDAwMDAwQDM2YmNkZWJmLTFlN2EtNGJhOC1hY2M1LTQ5NjgxZjY2ZDI0ZiIsImlhdCI6MTY1MzA0MjgyMSwibmJmIjoxNjUzMDQyODIxLCJleHAiOjE2NTMxMjk1MjEsImlkZW50aXR5cHJvdmlkZXIiOiIwMDAwMDAwMS0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDBAMzZiY2RlYmYtMWU3YS00YmE4LWFjYzUtNDk2ODFmNjZkMjRmIiwibmFtZWlkIjoiNjhjMDU2NmMtYjg1Mi00ZTI0LWI4NzktNzgxMDc3MjU2ZDA1QDM2YmNkZWJmLTFlN2EtNGJhOC1hY2M1LTQ5NjgxZjY2ZDI0ZiIsIm9pZCI6ImM4MWMyZmIyLTk0YmYtNDAyZi1hYzRlLWM0MmNmMTRkZGQ4NSIsInN1YiI6ImM4MWMyZmIyLTk0YmYtNDAyZi1hYzRlLWM0MmNmMTRkZGQ4NSIsInRydXN0ZWRmb3JkZWxlZ2F0aW9uIjoiZmFsc2UifQ.CzijGVkdhJAGebJfAn4CwM_ghRz_20iyuGsly9MK5zCGq233jl5_sW-ho8xXBAaPyjy5EstdeOWZT7l6pTOHomKdzqibmyrc96u5mokUgURY3GZfaRWUUOH0CVtxw9360fop2T04TamukELpl4e6c5cepyDAjgKgUM_QrQa65Il7T2bG1ojLkcwiywvMqIQorjBDeqM_PllWZ0d_lrPlPYTflNMSXSYzNqTg4f-ECnVheQnLHM_pu_WW54jNTVtzF2i0J6fArOI-KYILNfDOeM90Axm8LW0rwZ-Iu5jn9lTiB8tShr-I_sNtGG8VFD91lLh5oPwcd1EnjMVMB293Iw'
}

r = requests.get(r"path", headers=headers)
all = r.json()
rows = all["d"]["results"]
for row in rows:
    print(str(row["Title"])+ " | " + str(row["Test1"])+ " | "+ str(row["Test2"])+ " | "+ str(row["Test3"])+ " | "+ str(row["Test4"])+ " | "+ str(row["Test5"])+ " | "+ str(row["Test6"]))
