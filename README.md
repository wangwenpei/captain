# captain



## install depends

```

pip install -e .[dev]

```


## 指令说明


### 初始化

初始化会在当前项目下创建一个.kube-config目录

```
cap init ./  
```

参数：

- --template=git://github.com/wangwenpei/template  指定的模板目录


### patch

重新构建新的deployment

```

cap patch pod --namespace --context

```

### re-create

用于对daemon-set的重新发布

```

cap re-create daemon-set --namespace --context

```

### diff

用于比对多个环境不同的key-value结构

```

cap diff seed-dev seed-staging

```

参数：

- --with-content  比对内容，如果一样则抛出错误警告



### search

search 用于搜索caption官方仓库里的配置


