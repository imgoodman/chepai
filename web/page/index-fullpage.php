<?php
	header("content-type:text/html;charset=utf-8");
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>黄健的个人主页</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="黄健，个人网站，找工作,web,css,,html,javascript,js,.net,python,sql,data">
    <!--CSS-->
    <link rel="stylesheet" type="text/css" href="src/css/reset.css">
    <link rel="stylesheet" type="text/css" href="src/bootstrap-3.2.0-dist/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="src/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="src/css/infoTip.css">
	<link rel="stylesheet" type="text/css" href="src/fullPage/dist/jquery.fullpage.min.css">
    <link rel="stylesheet" type="text/css" href="src/css/main.css">

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
					<li><a href="#main_wrapper"><i class="fa fa-fw fa-home"></i>个人简介</a></li>
					<li><a href="#edu_wrapper"><i class="fa fa-fw fa-university"></i>教育背景</a></li>
					<li><a href="#research_wrapper"><i class="fa fa-fw fa-flask"></i>科学研究</a></li>
					<!-- <li><a href="info.php"><i class="fa fa-fw fa-tasks"></i>项目实践</a></li> -->
					<li><a href="#award_wrapper"><i class="fa fa-fw fa-star"></i>荣誉奖励</a></li>
					<li><a href="#paper_wrapper"><i class="fa fa-fw fa-book"></i>SCI论文</a></li>
					<li><a href="#skill_wrapper"><i class="fa fa-fw fa-code"></i>个人技能</a></li>
					<li><a href="#contact_wrapper"><i class="fa fa-fw fa-phone"></i>联系我</a></li>
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
	<div id="fullpage">
		<div class="section" style="background-colot:red;"></div>
		<div class="section" style="background-colot:green;"></div>
		<div class="section" style="background-colot:blue;"></div>
	</div>
	<div class="container-fluid" id="main_wrapper">
		<div class="row">
			<div class="col-md-3 col-md-offset-2 col-sm-5 text-center">
				<img src="src/img/Avatar.jpg" class="img-responsive" style="border-radius:50%;">
			</div>
			<div class="col-md-5 col-sm-7 text-center user_name">
				<h1>黄  健</h1>
				<h3>产品数据研发和AI爱好者<a href="mailto:iyangyang@sjtu.edu.cn" style="color:white; text-decoration:none;margin-left:10px;">iyangyang@sjtu.edu.cn</a></h3>
			</div>
		</div>
	</div>
	<div class="container-fluid" id="intro_wrapper">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>个人简介</h5>
			</div>
			<div class="col-md-6">
				<p>出色的课业成绩，学习能力强，与人为善，意志力坚韧，有团队精神和奉献精神</p>
			</div>
			<div class="col-md-3">
				<p>
					<a href="file/cv-huangjian.pdf" target="_blank"><i class="fa fa-download"></i>下载简历</a>
				</p>
			</div>
		</div>
	</div>
	<div class="container-fluid" id="edu_wrapper">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>教育背景</h5>
			</div>
			<div class="col-md-1">
				<img src="src/img/sjtu_logo2.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">上海交通大学  机械工程  硕博连读</h5>
				<h6>导师：谢友柏院士</h6>
				<h6 class="gpa_rank">GPA：2.88/3.3；专业排名：1/60</h6>
			</div>
			<div class="col-md-3">
				<p>
					<small>2008.9-2015.6</small>
				</p>
			</div>
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/whu_logo.gif" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">武汉大学  机械工程  学士</h5>
				<h6>GPA：3.78/4.0；专业排名：1/152</h6>
			</div>
			<div class="col-md-3">
				<p>
					<small>2004.9-2008.6</small>
				</p>
			</div>
		</div>
	</div>
	<!--researches-->
	<div id="research_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>科学研究</h5>
			</div>
			<div class="col-md-1">
				<img src="src/img/863.jpg" style="width:80px;height:60px;">
				<p><a href="info.php#p6" class="btn btn-default btn-xs" title="查看项目详细介绍">查看详情</a></p>
			</div>
			<div class="col-md-5">
				<h5 class="title_name">国家科技部863计划-支持多学科产品创新的概念设计关键技术与实现研究</h5>
				<h6>主要完成人</h6>
				<ul class="list">
					<li>提出基于本体的原理解表示方法，并通过输入/输出能量流来表示原理解的功能；</li>
					<li>提出原理解输入/输出接口属性及属性值匹配方法，来实现原理解综合集成，获得创新的产品结构；</li>
					<li>采用深度优先算法和多Agent方法，来提高原理解搜索效率。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2008.5-2010.11</small></p>
			</div>

			<!-- second research-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/nsf.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">国家自然基金-基于Affordance的详细设计知识建模、捕获与重用方法研究</h5>
				<h6>主要完成人</h6>
				<ul class="list">
					<li>将心灵哲学中的Affordance概念，经过澄清，运用到详细设计阶段；</li>
					<li>提出广义的面向详细设计阶段的基于本体的功能概念；</li>
					<li>提出面向产品全生命周期的设计知识表示模型。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2014.1-2017.12</small></p>
			</div>

			<!-- third research-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/nsf.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">上海市科技启明星计划-设计知识的建模与重用方法及其子车身设计中的应用研究</h5>
				<h6>主要完成人</h6>
				<ul class="list">
					<li>提出基于本体的行为表示方法，用于表示机械设计零部件的行为知识；</li>
					<li>提出基于Affordance的功能表示方法，用于表示机械设计零部件的功能知识，并导出设计约束；</li>
					<li>提出基于FBA的设计详细知识模型，提高了设计知识的重用效率20%。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2009.7-2011.6</small></p>
			</div>
		</div>
	</div>
	<!--projects-->
	<div id="project_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>项目实践</h5>
			</div>
			<div class="col-md-1">
				<img src="src/img/comac_logo.jpg" style="width:60px;height:60px;">
				<p><a href="info.php#p5" class="btn btn-default btn-xs" title="查看项目详细介绍">查看详情</a></p>
			</div>
			<div class="col-md-5">
				<h5 class="title_name">中国商飞上海飞机设计研究院-基于知识的适航取证智能预规划方法与实现研究</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用.Net, Ajax, jQuery等技术，开发基于Web适航取证数据管理系统，实现百万级数据有效管理；</li>
					<li>开发支持上百种ARJ型号取证数据类型的动态表单表示模型，实现取证文档数据的动态管理；</li>
					<li>在大量取证数据基础上，开发知识挖掘系统，为ARJ型号构型知识管理提供帮助。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2013.9-2015.3</small></p>
			</div>

			<!-- second project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/comac_logo.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">中国商飞上海飞机设计研究院-面向设计过程的适航要求识别、分解与确认系统</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用.Net, MS SQL技术，建立基于Web适航审定知识库，代替目前完全依靠适航工程师逐条解读；</li>
					<li>开发辅助工具，来帮助适航工程师完成试航标准的分解、传递及关联分析，避免适航要求的疏漏；</li>
					<li>开发搜索算法和智能匹配方法，来帮助适航工程师更加高效准确地对适航条款解读及确认。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2011.3-2013.7</small></p>
			</div>

			<!-- third project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/csr.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">中国南车戚墅堰机车有限公司-夹具设计知识管理及Pro/E二次开发集成</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用.Net, MS SQL, C++技术，开发基于Web和CAD的夹具设计知识管理系统；</li>
					<li>独立开发基于Web夹具设计知识管理系统，捕获设计专家设计知识，申请软件著作权两项；</li>
					<li>独立开发基于C++和Pro/E API的知识驱动的模型再生系统，使夹具设计周期缩短60%。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2010.5-2011.6</small></p>
			</div>

			<!-- fourth project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/csr.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">中国南车戚墅堰机车有限公司-汽车配件工艺开发管理信息系统</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用ASP.NET和SQL Server工具，独立开发动态的工作流引擎，优化工艺开发信息传递方式，使开发周期缩短25%；</li>
					<li>独立开发工艺文档审核和校核模板，提高工艺开发效率15%。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2009.1-2009.12</small></p>
			</div>

			<!-- fifth project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/ruitao2.jpg" style="width:60px;height:60px;">
				<p><a href="info.php#p1" class="btn btn-default btn-xs" title="查看项目详细介绍">查看详情</a></p>
			</div>
			<div class="col-md-5">
				<h5 class="title_name">上海睿涛信息科技有限公司-室内空气净化，楼宇能耗监控，机床误差补偿系统</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>独立开发基于Web室内空气净化系统，控制新风系统工作状态，实现室内空气质量监测；</li>
					<li>独立开发基于Web办公楼宇能耗监控平台，实时监测能耗指标，为节能提供指导；</li>
					<li>独立开发基于Web数控机床热误差补偿监测系统，实现机床信息的集中监测与控制。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2013.5-2014.12</small></p>
			</div>

			<!-- sixth project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/mahle.jpg" style="width:60px;height:60px;">
			</div>
			<div class="col-md-5">
				<h5 class="title_name">马勒技术投资（中国）有限公司-财务部门办公自动化系统</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用C#，WPF，MS Access和XML技术，独立开发动态的办公自动化辅助工具，减少日常重复工作，提高工作效率达60%；</li>
					<li>自动地并可定制地导出公司财务报表（资产负债表，成本计划等）。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2012.6-2013.10</small></p>
			</div>

			<!-- seventh project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/sjtu_logo2.jpg" style="width:60px;height:60px;">
				<p><a href="info.php#p2" class="btn btn-default btn-xs" title="查看项目详细介绍">查看详情</a></p>
			</div>
			<div class="col-md-5">
				<h5 class="title_name">上海交通大学先进产业技术研究院-协同创新平台</h5>
				<h6>前端开发</h6>
				<ul class="list">
					<li>采用CSS3, jQuery技术，开发基于Web的协同创新平台(www.innoxyz.com)的前端;</li>
					<li>采用Java的Struts框架和MySQL数据库，开发后台业务功能（好友，私信，项目等）。</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2011.8-2012.5</small></p>
			</div>

			<!-- eighth project-->
			<div class="col-md-1 col-md-offset-3">
				<img src="src/img/logo.png" style="width:60px;height:60px;">
				<p><a href="info.php#p3" class="btn btn-default btn-xs" title="查看项目详细介绍">查看详情</a></p>
			</div>
			<div class="col-md-5">
				<h5 class="title_name">上海林康医疗信息技术有限公司-医院信息管理系统</h5>
				<h6>开发负责人</h6>
				<ul class="list">
					<li>采用ASP.NET和SQL Server技术，独立开发患者信息管理系统，跟踪患者的随访记录；</li>
					<li>动态导出相关报表（患者信息，药物治疗效果比较等）；</li>
				</ul>
			</div>
			<div class="col-md-3">
				<p><small>2010.10-2011.7</small></p>
			</div>

		</div>
	</div>
	<!--awards-->
	<div id="award_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>荣誉奖励</h5>
			</div>
			<div class="col-md-9">
				<div class="row">
					<div class="col-md-2">
						<img src="src/img/sjtu_logo2.jpg" style="width:60px;height:60px;">
					</div>
					<div class="col-md-6">
						<h5>上海交通大学光华一等奖学金</h5>
					</div>
					<div class="col-md-3">
						<p><small>2010.6</small></p>
					</div>
					<div class="col-md-6">
						<h5>现代设计研究所羽毛球比赛男子单打冠军</h5>
					</div>
					<div class="col-md-3">
						<p><small>2012.5</small></p>
					</div>
				</div>
				<div class="row">
					<!-- second award-->
					<div class="col-md-2">
						<img src="src/img/whu_logo.gif" style="width:60px;height:60px;">
					</div>
					<div class="col-md-10">
						<div class="row">
							<div class="col-md-7">
								<h5>武汉大学国家奖学金</h5>
							</div>
							<div class="col-md-5">
								<p><small>2007.12</small></p>
							</div>
							<div class="col-md-7">
								<h5>武汉大学优秀毕业生</h5>
							</div>
							<div class="col-md-5">
								<p><small>2008.4</small></p>
							</div>
							<div class="col-md-7">
								<h5>武汉大学三好学生</h5>
							</div>
							<div class="col-md-5">
								<p><small>2007.10</small></p>
							</div>
							<div class="col-md-7">
								<h5>武汉大学乙等奖学金，连续四次</h5>
							</div>
							<div class="col-md-5">
								<p><small>2005-2008</small></p>
							</div>
						</div>
					</div>

				</div>
			</div>
		</div>

	</div>
	<!--publications-->
	<div id="paper_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>SCI论文</h5>
			</div>
			<div class="col-md-2 text-center">
				<img src="src/img/cera.jpg" class="img-responsive">
				<h6><a href="http://cer.sagepub.com/content/22/4/291" target="_blank">A part affordance–based approach for detailed design process planning in collaborative environment</a></h6>
			</div>
			<div class="col-md-2 text-center">
				<img src="src/img/partc.png" class="img-responsive">
				<h6><a href="http://pic.sagepub.com/content/early/2015/04/06/0954406215578702.full.pdf+html" target="_blank">An integrated knowledge-based framework for design reuse</a></h6>
			</div>
			<div class="col-md-2 text-center">
				<img src="src/img/cad.gif" class="img-responsive">
				<h6><a href="http://www.sciencedirect.com/science/article/pii/S0010448513001450" target="_blank">A part affordance-based approach for capturing detailed design knowledge</a></h6>
			</div>
			<div class="col-md-2 text-center">
				<img src="src/img/AIE.jpg" class="img-responsive">
				<h6><a href="http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=9049254&fulltextType=RA&fileId=S0890060413000164" target="_blank">Modeling detailed design knowledge based on an Extended Structure-Behavior-Function Model</a></h6>
			</div>
		</div>
	</div>
	<!--skills-->
	<div id="skill_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>个人技能</h5>
			</div>
			<div class="col-md-5">
				<h5>熟练掌握</h5>
				<div class="row">
					<div class="col-lg-2">
						<img src="src/img/net.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/mssql.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/java.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/mysql.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/html.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/js.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/css.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/jquery.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-2">
						<img src="src/img/bootstrap.jpg" class="img-responsive img-rounded">
					</div>
				</div>
				
				<!-- <canvas id="radar"  width="400" height="410"></canvas> -->
			</div>
			<div class="col-md-3 col-md-offset-1">
				<h5>基本了解</h5>
				<div class="row">
					<div class="col-lg-4">
						<img src="src/img/python.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-4">
						<img src="src/img/nodejs.jpg" class="img-responsive img-rounded">
					</div>
					<div class="col-lg-4">
						<img src="src/img/vuejs.png" class="img-responsive img-rounded">
					</div>
				</div>
			</div>
			<!-- <div class="col-md-2 text-center">
				<h5>感兴趣的</h5>
				<img src="src/img/h5.jpg">
				<img src="src/img/nodejs.jpg">
				<img src="src/img/android.jpg">
				<img src="src/img/ios.jpg">
			</div> -->
		</div>
	</div>
	<!--contact me-->
	<div id="contact_wrapper" class="container-fluid">
		<div class="row">
			<div class="col-md-2 col-md-offset-1">
				<h5>联系我</h5>
			</div>
			<div class="col-md-6">
				<p class="pretitle"><i class="fa fa-pencil"></i>邮箱</p>
				<p><a href="mailto:iyangyang@sjtu.edu.cn">iyangyang@sjtu.edu.cn</a></p><br>
				<p class="pretitle"><i class="fa fa-location-arrow"></i>地址</p>
				<p>上海市闵行区东川路</p>
			</div>
			<div class="col-md-2 text-center">
				<h5>社交网络</h5>
				<p>
					<a href="http://weibo.com/iyangyanga" target="_blank" title="新浪微博"><i class="fa fa-2x fa-weibo" style="color:#E74C3C;"></i></a>
					<a href="http://www.linkedin.com/in/jian-huang-264a0b39" target="_blank" title="linkedin"><i class="fa fa-2x fa-linkedin-square" style="color:#23639a;"></i></a>
				</p>
				<img src="src/img/weixin.jpg" style="width:120px;height:120px;">
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
        <a href="#main_wrapper"><i class="fa fa-arrow-up"></i>返回顶部</a>
    </div>
		<!--js-->
		<!--[if lt IE 9]>
		<script type="text/javascript" src="src/js/html5shiv.min.js"></script>
		<script type="text/javascript" src="src/js/respond.min.js"></script>
		<![endif]-->
		<script type="text/javascript" src="src/js/jquery-1.11.0.min.js"></script>
		<script type="text/javascript" src="src/bootstrap-3.2.0-dist/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="src/js/infoTip.js"></script>
		<script type="text/javascript" src="src/fullPage/dist/jquery.fullpage.min.js"></script>
		<script type="text/javascript" src="src/chartjs/Chart.min.js"></script>
		<script type="text/javascript" src="src/js/smoothscroll.js"></script>
	<script type="text/javascript">
		$(document).ready(function(){

			$("#fullpage").fullpage();
			//cet6
			/*var doughnutDataCet6 = [{value: 85,color:"#1abc9c"},{value : 15,color : "#ecf0f1"}];
			var ctxCet6 = document.getElementById("cet6").getContext("2d");
			new Chart(ctxCet6).Doughnut(doughnutDataCet6);
			//germany
			var doughnutDataGermany = [{value: 70,color:"#1abc9c"},{value : 30,color : "#ecf0f1"}];
			var ctxGermany = document.getElementById("germany").getContext("2d");
			new Chart(ctxGermany).Doughnut(doughnutDataGermany);
			//aspnet
			var doughnutDataAspnet = [{value: 90,color:"#1abc9c"},{value : 10,color : "#ecf0f1"}];
			var ctxAspnet = document.getElementById("aspnet").getContext("2d");
			new Chart(ctxAspnet).Doughnut(doughnutDataAspnet);*/

			//radar
			/*var data = {
						labels : ["ASP.NET","MS SQL","Java","PHP","mySQL","javascript","CSS","python"],
						datasets : [
								{
									fillColor : "rgba(151,187,205,0.5)",
									strokeColor : "rgba(151,187,205,1)",
									pointColor : "rgba(151,187,205,1)",
									pointStrokeColor : "#fff",
									data : [85,75,75,70,75,80,80,70]
								}]
						};
			var ctxRadar = document.getElementById("radar").getContext("2d");
			new Chart(ctxRadar).Radar(data);*/
		});
	</script>
</body>
</html>
