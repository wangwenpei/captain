# Kaptain

A modern SRE tool.


### Install

```

pip install kaption

```

### Support version

    python 3.5+



### report


report operation to platform, currently it only support slack.


#### pre-config

we need `.git-config` to set user/email. 

```
vi ~/.gitconfig

# add line like this

[kaption]
        slack-channel = https://hooks.slack.com/xxx
        slack-private = https://hooks.slack.com/xxx

```

#### how to

```
kap report "hello world" --private   # send to private channel 

kap report "hello world"             # send to public channel 

```
