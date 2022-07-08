# list-tags-to-promote

This generates lines for [promoter configurations](https://github.com/kubernetes/k8s.io/blob/main/k8s.gcr.io/images/k8s-staging-networking/images.yaml).

## Usage

```
$ ./promote.py gcr.io/k8s-staging-networking/ip-masq-agent v2.7.0 --indent=4
    "sha256:5cef04a18d5563913bd944270796f8f3f150c390dd0c61a357c936cae011acd3": ["v2.7.0"]
    "sha256:f74c84736e025bcca1c8657573ca761dbc5b731aebdc0be3d01efb9c13d50c49": ["v2.7.0__linux_amd64"]
    "sha256:6f788808af0aee7674d051044d162a9d8b72d7c4668ed0ac9aca748b2d47b0b8": ["v2.7.0__linux_arm"]
    "sha256:0224cbadd17ebfb0c1a7946c556bee7ec00613f11e4ee98deb10264de64b72c1": ["v2.7.0__linux_arm64"]
    "sha256:6b140e992a17f88a2fe35db20a15b626b17464fe7ef6b69b2c8cbfaae49da5df": ["v2.7.0__linux_ppc64le"]
    "sha256:24be0d068a976e7d015c50ba853dabd59cc67c9c22493b272730e8289c970ae2": ["v2.7.0__linux_s390x"]
```
