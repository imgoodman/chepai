<?php
	header("content-type:text/html;charset=utf-8");
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>黄健的个人主页</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--CSS-->
    <link rel="stylesheet" type="text/css" href="src/css/reset.css">
    <link rel="stylesheet" type="text/css" href="src/bootstrap-3.2.0-dist/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="src/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="src/css/infoTip.css">
    <link rel="stylesheet" type="text/css" href="src/css/main.css">
    <!--js-->
    <!--[if lt IE 9]>
		<script type="text/javascript" src="src/js/html5shiv.min.js"></script>
		<script type="text/javascript" src="src/js/respond.min.js"></script>
    <![endif]-->
    <script type="text/javascript" src="src/js/jquery-1.11.0.min.js"></script>
    <script type="text/javascript" src="src/bootstrap-3.2.0-dist/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="src/js/infoTip.js"></script>
    <script type="text/javascript" src="src/chartjs/Chart.min.js"></script>
    <script type="text/javascript" src="src/js/smoothscroll.js"></script>
</head>
<body>
    <div class="navbar navbar-default navbar-fixed-top">
        <div class="navbar-fluid" style="padding-left:20px;padding-right:20px;">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span><span
                        class="icon-bar"></span><span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.php">Wellman</a>
            </div>
            <div class="navbar-collapse collapse" id="navbar">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="index.php#main_wrapper"><i class="fa fa-home"></i>个人简介</a></li>
                    <li><a href="index.php#edu_wrapper"><i class="fa fa-university"></i>教育背景</a></li>
                    <li><a href="index.php#research_wrapper"><i class="fa fa-flask"></i>科学研究</a></li>
                    <!-- <li><a href="index.php#project_wrapper"><i class="fa fa-tasks"></i>项目实践</a></li> -->
                    <li><a href="index.php#award_wrapper"><i class="fa fa-star"></i>荣誉奖励</a></li>
                    <li><a href="index.php#paper_wrapper"><i class="fa fa-book"></i>SCI论文</a></li>
                    <li><a href="index.php#skill_wrapper"><i class="fa fa-code"></i>个人技能</a></li>
                    <li><a href="index.php#contact_wrapper"><i class="fa fa-phone"></i>联系我</a></li>
                    <li role="presentation" class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                            <i class="fa fa-fw fa-tasks"></i>项目实践<span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" role="menu">
                            <li><a href="info.php">承担课题</a></li>
                            <li class="divider"></li>
                            <li><a href="chepai/ml.html">机器学习拍卖数据</a></li>
                            <li><a href="chepai/chepai.html">爬虫拍卖数据</a></li>
                            <li class="divider"></li>
                            <li><a href="h5/h5-digital.html">Html5计时器</a></li>
                            <li><a href="h5/canvas/star-standard.html">Html5夜空</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row content_wrapper" id="info_wrapper">
            <div class="col-md-4 col-md-offset-1">
                <p>在上海交通大学硕博连读几年中，负责或者参与过10余个项目，现根据项目的对象，所在领域和技术路线，选取其中6个典型的项目进行简要介绍，并从项目的目标，实现目标的技术路线，本人在项目中起到的角色作用和项目的示例用户界面这4个方面来阐述。这6个项目分别如右所示。其中，前4个项目是业余时间参加的项目，而后2个项目是实验室课题组的项目。这些项目的简要介绍如下所述。</p>
            </div>
            <div class="col-md-6">
                <ul class="list">
                    <li><a href="#p1">上海睿涛信息科技有限公司－－室内空气净化，楼宇能耗监控，机床热误差补偿系统</a></li>
                    <li><a href="#p2">上海交通大学先进产业技术研究院－－协同创新平台</a></li>
                    <li><a href="#p3">上海林康医疗信息技术有限公司－－医院风湿病随访随访管理系统</a></li>
                    <li><a href="#p4">湖南长沙三一重工－－分布式资源环境平台</a></li>
                    <li><a href="#p5">中国商飞上海飞机设计研究院－－基于知识的适航取证智能预规划方法和实现研究</a></li>
                    <li><a href="#p6">国家科技部863计划－－支持多学科产品创新的概念设计关键技术与实现研究</a></li>
                </ul>
            </div>
        </div>
        <div class="row content_wrapper" id="p1">
            <div class="col-md-10 col-md-offset-1">
                <h3>上海睿涛信息科技有限公司-－室内空气净化，楼宇能耗监控，机床热误差补偿系统</h3>
            </div>            
            <div class="col-md-5 col-md-offset-1">
                
                <dl>
                    <dt>项目目标</dt>
                        <dd>此项目包括3个子项目，分别是：室内环境净化控制管理系统，建筑能耗监管信息平台，和数控机床热误差补偿群控系统。<br>室内环境净化控制管理系统目前运行在德威国际学校（苏州和上海）。该系统的目的是在合理控制滤芯工作时间情况下，为室内的人们提供健康的环境（主要是空气过滤）。<br>建筑能耗监管信息平台目前运行在舟山市某政府大楼。该平台的目的是相应国家节能减排号召，先期对办公楼宇的能耗进行监管，为后期提供节能整改措施提供咨询依据。<br>数控机床热误差补偿群控系统目前运行于沈阳第一机床厂的某车间。该平台的目的是通过监控数控机床的关键部件的温度变化情况，为热误差补偿模型提供数据基础，从而提高机床的加工精度。</dd>
                    
                </dl>
            </div>
            <div class="col-md-5">
                <dl>
                    <dt>项目技术路线</dt>
                        <dd>该项目采用的技术有：php，mysql，jQuery，ajax，json，css，bootstrap，fontawesome。前端采用bootstrap框架进行布局，并通过jQuery + ajax 从后端获取json数据，来渲染页面显示，后端的业务逻辑处理是通过php来实现，数据存储在mysql数据库中。系统运行于wamp环境下。</dd>
                    <dt>个人的角色</dt>
                        <dd>个人是该项目的独立开发负责人，包括数据库建模，业务逻辑处理，前端布局显示。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p11">
            <div class="col-md-7 col-md-offset-1">
                <img src="src/img/p11.png" class="img-responsive">
            </div>
            <div class="col-md-3">
                <p>室内环境净化控制管理系统的核心功能模块是：房间的控制信息管理模块。<br>在滤芯失效后，更换滤芯，用户可以重置滤芯工作时间。并且，为了延长昂贵的滤芯的工作时间，用户可以指定新风系统的开关机时间（比如，从早上7点到下午5点）。<br>同时，用户可以查看到房间的控制系统当前运行状态。通过操作控制面板来控制房间的控制模式（手动和自动）。并且，用户可以通过页面上的图标（风机，风阀等）直观地控制房间的控制状态，并实时查看到房间的运行状态。</p>
            </div>
        </div>
        <div class="row content_wrapper" id="p12">
            <div class="col-md-3 col-md-offset-1">
                <p>建筑能耗监管信息平台的典型功能模块是：楼宇的能耗分析对比功能模块。<br>通过安装在智能终端（智能电表等）的监测设备，将房间的能耗（水，点，气，热）数据汇总到数据中心。用户从时间，分类分项，区域，房间灯方面，分析其能耗数据，生成相应的对比曲线。为后期的节能改造提供咨询依据。</p>
            </div>
            <div class="col-md-7">
                <img src="src/img/p12.png" class="img-responsive">
            </div>
        </div>
        <div class="row content_wrapper" id="p13">
            <div class="col-md-7 col-md-offset-1">
                <img src="src/img/p13.png" class="img-responsive">
            </div>
            <div class="col-md-3">
                <p>数控机床热误差补偿群控系统主要功能模块：机床关键部件温度曲线分析，如图3所示，该曲线是采用highstock控件来显示的。<br>根据安装在机床关键部件（丝杆螺母，轴承等）的传感器设备，将其实时采集的温度数据通过TCP/IP发送到数据中心。服务器的数据接收程序将数据进行离散处理，存储在数据库中，供后期的温度数据分析。用户可以根据机床，机床轴，轴的核心部件，时间区间来查找相关的温度数据，形成变化曲线。</p>
            </div>
        </div>

        <!--second project-->
        <div class="row content_wrapper" id="p2">
            <div class="col-md-10 col-md-offset-1">
                <h3>上海交通大学先进产业技术研究院－－协同创新平台</h3>
                <dl>
                    <dt>项目目标</dt>
                        <dd>该项目目前主要服务于上海交通大学校内研究机构，目的是为了解决高校内部资源的重复建设问题，提高多学科交叉项目的协同创新。</dd>
                    <dt>项目技术路线</dt>
                        <dd>该项目的1.0版本已经上线，地址为:www.innoxyz.com，首页如图4所示。采用java + struts2 MVC架构，mysql作为关系型数据库，tomcat作为web服务器，前端采用jQuery，css，less等技术。</dd>
                    <dt>个人的角色</dt>
                        <dd>该项目是由上海交通大学计算机系相关的同学主导开发，个人参与其中的部分功能模块的前端开发，包括用户个人主页（教育经历，项目经理，技能等），站内信功能（收发消息），和个人名片功能（类似于weibo个人简介弹出框）。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p21">
            <div class="col-md-3 col-md-offset-1">
                <p>机构可以在平台上发布项目，上传文档，管理项目进度等。个人可以申请加入项目，成为项目组成员，共享项目组内信息和资源。同时，个人可以将创新的想法发布在平台上，相关用户可以补充，讨论这些想法，积极将比较新颖的想法逐渐完善，成为创新的项目。然后，在平台上邀请相关领域的用户加入到项目实践中，提高创新成果的转化效率。</p>
            </div>
            <div class="col-md-7">
                <img src="src/img/p21.png" class="img-responsive">
            </div>
        </div>

        <!--third project-->
        <div class="row content_wrapper" id="p3">
            <div class="col-md-10 col-md-offset-1">
                <h3>上海林康医疗信息技术有限公司－－医院风湿病随访随访管理系统</h3>
                <dl>
                    <dt>项目目标</dt>
                        <dd>对于慢性病患者，医生跟踪患者的随访信息，可以针对治疗效果，更合理地知道用药策略。</dd>
                    <dt>项目技术路线</dt>
                        <dd>该项目采用典型的三层架构，如图5所示。采用MS SQL SERVER作为关系型数据库，采用LINQ to SQL和C#作为数据读写和业务逻辑处理，采用ASP.NET和Dev Express作为用户界面构建。</dd>
                    <dt>个人的角色</dt>
                        <dd>与其他两个工程师一起完成项目开发，个人负责Web端的用户交互。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p31">            
            <div class="col-md-7 col-md-offset-1">
                <img src="src/img/p31.jpg" class="img-responsive">
            </div>
            <div class="col-md-3">
                <p>医院的医生可以导入目前的药物列表，疾病症状列表，患者基本信息，患者的随访信息。</p>
            </div>
        </div>

        <!--fourth project-->
        <div class="row content_wrapper" id="p4">
            <div class="col-md-10 col-md-offset-1">
                <h3>湖南长沙三一重工－－分布式资源环境平台</h3>
                <dl>
                    <dt>项目目标</dt>
                        <dd>大型企业内部资源存在重复建设，利用率不高，专业人员的知识有限，产品协同开发困难。分布式资源环境平台将企业内部的知识资源，硬件软件资源连接起来，提高产品创新设计中的协同设计过程。</dd>
                    <dt>项目技术路线</dt>
                        <dd>该项目采用典型的三层架构，如图6所示，其中MS SQL SERVER作为关系型数据库，通过C#和LINQ to SQL读取数据，并进行相应的业务逻辑处理，再通过通用句柄ashx将处理后的数据以json的方式返回给前端，前端采用jQuery，css等技术渲染用户界面。</dd>
                    <dt>个人的角色</dt>
                        <dd>该项目是个人独立开发完成，负责数据模型的建立，业务逻辑的编写和测试，前端用户界面的布局和渲染。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p41">
            <div class="col-md-3 col-md-offset-1">
                <p>企业内部机构可以在平台上发布知识服务，并结构化服务的内容，包括服务需要的输入条件，以及服务输出的结果。其他内部机构可以在平台上检索相关的知识服务，并请求这些知识服务。提供相应的必须输入条件后，待服务提供方确认后，正式进入服务的过程。知识提供方和知识请求方都可以在平台上查看到服务的进度，服务的结果，对服务结果的满意程度，直到达成一致意见，形成完善的服务结果。</p>
            </div>
            <div class="col-md-7">
                <img src="src/img/p41.png" class="img-responsive">
            </div>
        </div>

        <!--fifth project-->
        <div class="row content_wrapper" id="p5">
            <div class="col-md-10 col-md-offset-1">
                <h3>中国商飞上海飞机设计研究院－－基于知识的适航取证智能预规划方法和实现研究</h3>
                <dl>
                    <dt>项目目标</dt>
                        <dd>国内正在大力发展民机行业，目前正在研制的ARJ型号飞机是非常复杂的工业产品。要使得ARJ飞机适用于商业运营，就必须满足FAA（美国联邦航空局）和CAAC（中国民用航空局）规定的一系列适航取证要求。该项目的目的是通过将适航取证要求结构化，帮助飞机设计人员及时地发现功能要求，降低设计反复。并且为民航局的ARJ型号取证提供完整的设计依据。</dd>
                    <dt>项目技术路线</dt>
                        <dd>该项目采用典型的三层架构，如图7所示，其中MS SQL SERVER作为关系型数据库，通过C#和Ado.net读取数据，并进行相应的业务逻辑处理，再通过通用句柄ashx将处理后的数据以json的方式返回给前端，前端采用jQuery，css等技术渲染用户界面。</dd>
                    <dt>个人的角色</dt>
                        <dd>该项目是个人独立开发完成，负责数据模型的建立，业务逻辑的编写和测试，前端用户界面的布局和渲染。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p51">            
            <div class="col-md-7 col-md-offset-1">
                <img src="src/img/p51.jpg" class="img-responsive">
            </div>
            <div class="col-md-3">
                <p>由于适航取证数据涉及面非常广（上百种设计文档资料），因此，取证数据的结构差异性较大。该系统允许系统管理者根据业务需求，自定义设计文档资料的属性结构。并通过系统的动态表单功能模块将自定义的数据表单呈现给用户。同时，根据不同的数据类型（日期，文本，多文本，人员，多人组合，部门，枚举类型，关联对象等），渲染出不同的效果，并验证用户提交数据的有效性和合法性。</p>
            </div>
        </div>

        <!--sixth project-->
        <div class="row content_wrapper" id="p6">
            <div class="col-md-10 col-md-offset-1">
                <h3>国家科技部863计划－－支持多学科产品创新的概念设计关键技术与实现研究</h3>
                <dl>
                    <dt>项目目标</dt>
                        <dd>产品创新所面临的主要问题是产品设计往往需要多学科知识，而设计人员往往只是专注于较少领域知识。因此，该项目的目的是帮助设计人员根据功能要求，智能地检索到多学科的原理解决方案，并将它们综合成创新产品的原型模型。</dd>
                    <dt>项目技术路线</dt>
                        <dd>该项目采用典型的三层架构，采用MS SQL SERVER作为关系型数据库，采用LINQ to SQL和C#作为数据读写和业务逻辑处理，采用ASP.NET作为用户界面构建。通过深度优先算法，从知识库中检索满足功能要求的综合设计解方案。</dd>
                    <dt>个人的角色</dt>
                        <dd>该项目是个人独立开发完成，负责数据模型的建立，设计知识的表示模型，算法的实现，业务逻辑的编写和测试，前端用户界面的设计。</dd>
                </dl>
            </div>
        </div>
        <div class="row content_wrapper" id="p61">
            <div class="col-md-3 col-md-offset-1">
                <p>该系统的主要功能模块：设计求解方案的检索和综合，如图8，9，10所示。
    其中，通过C#实现深度优先算法的主要思路是，根据原始功能需求，从知识库中检索满足输入功能要求的解方案，如果检索到的解方案不符合设计要求，则根据当前解方案的输出，从知识库中检索到满足要求的解方案，并将该解方案作为上述解方案的子节点。如此反复，形成多层二叉树，当检索深度达到指定要求，则从二叉树的底部开始向上回溯，将满足要求的解方案链条输出。
</p>
            </div>
            <div class="col-md-7">
                <img src="src/img/p61.jpg" class="img-responsive">
            </div>
        </div>
        <div class="row content_wrapper" id="p62">            
            <div class="col-md-5 col-md-offset-1">
                <img src="src/img/p62.jpg" class="img-responsive">
            </div>
            <div class="col-md-5">
                <img src="src/img/p63.jpg" class="img-responsive">
            </div>
        </div>      

    </div>
    <div class="container-fluid text-center" id="footer">
        <div class="col-md-12">
            <p>本站基于Bootstrap开发，支持PC端，移动端的浏览</p>
            <p>
                版权所有，已备案<a href="http://www.miitbeian.gov.cn/" target="_blank">沪ICP备14054017号</a>
            </p>
        </div>
    </div>
    <div class="btn btn-primary" style="display:block;position:fixed;right:10px;bottom:10px;">
        <a href="#info_wrapper"><i class="fa fa-arrow-up"></i>返回顶部</a>
    </div>
</body>