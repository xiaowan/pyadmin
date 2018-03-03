**简介**
该脚手架可快速为管理后台提供restful接口，框架前端使用 https://github.com/PanJiaChen/vue-element-admin  
框架自带一个简单的RBAC以及web操作界面，web界面地址：https://github.com/xiaowan/pyadmin-ui  
数据库表及部分数据在dbinfo 目录内  
测试数据中包含三个用户，登陆名为root，developer，seven，分别对应 上帝视角，开发人员，普通员工三个系统角色  


**要求python版本为3.5+，使用到的第三方库：**  
 - tornado 作为基础框架
 - oslo.config 作为配置管理
 - oslo.context 作为请求分配request id，如果以后收集日志至类似ELK环境中，可使用request id 来查询  
 - oslo.log 日志管理
 - sqlalchemy 作为mysql mapper
 - pika 操作rabbitmq
 - redis 操作redis，目前登陆token存放在redis中

  

**配置环境**
此脚手架使用openstack的 oslo.config 作为配置管理，目前区分三个环境，分别是线上环境(conf)，开发环境(debug)，预览环境(pre)。 指定环境有三种方式：  

 - 项目启动时使用 --config-file=conf/xxx.ini 来读取指定配置。  
 - 设置 UNITYMOB_ENVIRON 环境变量，变量值分别为 conf, debug, pre ，分别对应上述三个环境。  
 - 如果不指定配置文件，也没有设置环境变量，则默认使用conf环境的配置。  
如果同时设置了方式一和方式二，方式一的优先级级别最高。 

**关于目录结构**
个人更喜欢java工程目录接口，所以该脚手架很大一部分都借鉴了java工程，以下为脚手架目录结构  
 - controllers 请求地址与逻辑类映射 service
 - 业务逻辑层，被controller层调用
 - dao 细粒度的数据库增删改查
 - mapper 中每个文件为数据库表对应的文件
 - conf 存放所有配置文件。
 - library 目录为经常用到的库，以及常用中间件的简单封装，大致内容为：  

&nbsp;&nbsp;Decoreate.py 常用装饰器  
&nbsp;&nbsp;Exception.py 在这里自定义自己的异常，使用时只需在代码中抛出该异常即可。  
&nbsp;&nbsp;G.py 这是一个单例类，常用的中间件都会放到此类中操作。  
&nbsp;&nbsp;Handlers.py 业务层Handler，controllers中的具体操作类可根据具体情况继承该文件中的Handler。  
&nbsp;&nbsp;MyRabbitmq.py rabbitmq 操作封装，尽可能使用一个rabbitmq连接，每个请求中使用一个单独的channel操作rabbitmq  
&nbsp;&nbsp;MyRedis.py redis操作封装  
&nbsp;&nbsp;Result.py restful请求返回结果封装  
&nbsp;&nbsp;Route.py 负责管理所有的请求地址与逻辑处理类的映射
&nbsp;&nbsp;RPCClient.py 暂时无用  
&nbsp;&nbsp;Utils.py 常用工具类函数  

**以下为常用装饰器：**  

 - DI 使用了python动态语言的特性，可以方便的为类新增类属性。
 - Singleton 单例模式
 - Transaction 需要使用事务的地方，函数执行结束会自动提交事务，如执行失败会上抛该函数异常，并且回滚事务。
 - Return controller层返回结果的封装，确保返回结果被放到了Result类中
 - Deprecated 已废弃方法如果代码没有及时删除，可使用该装饰器提示。
 
 ---

部分功能截图如下：
![image](https://github.com/xiaowan/pyadmin/blob/master/snapshot/WechatIMG140.jpeg)

![image](https://github.com/xiaowan/pyadmin/blob/master/snapshot/WechatIMG141.jpeg)

![image](https://github.com/xiaowan/pyadmin/blob/master/snapshot/WechatIMG142.jpeg)

![image](https://github.com/xiaowan/pyadmin/blob/master/snapshot/WechatIMG143.jpeg)

![image](https://github.com/xiaowan/pyadmin/blob/master/snapshot/WechatIMG139.jpeg)
 
