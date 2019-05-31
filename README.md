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


#### Fetch GCP Log


##### Pre-Requirements

- gcloud cli


```
export KAPTAIN_FETCH_LOG_PROJECT=YOUR-GCP-PROJECT-ID

# preview  
kap fetch-log gcp abc.log  --save-dir=$HOME/Downloads --display --filter=tradebot-prod --date-filter=2019/05/30 --bucket-name=archive-log

# download
kap fetch-log gcp abc.log  --save-dir=$HOME/Downloads --filter=tradebot-prod --date-filter=2019/05/30 --bucket-name=archive-log

```
