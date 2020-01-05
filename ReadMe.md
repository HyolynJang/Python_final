### HTML档描述
* 所有的html文档存放于templates文件下，并将html格式的图分别置于fp与llh两个文件夹下
* base.html为results.html的基模板，其他res.html均对应不同选项的输出页面

1.Templates
    1.fp（扶贫）
        1.fp_dbcomparison.html （GDP、农村城市低保的对比）
        2.fp_czkzp.html （城镇农村人均可支配收入）
        3.fp_gdp.html (2011年分省GDP)
        4.fp_rural_security.html （历年中国各省农村最低生活保障人数）
        5.fp_city_security.html（历年中国各省城市最低生活保障人数）
        6.fp_job_trend.html （乡就业人员的变化）
    2.llh（老龄化）
        1.llh_rate_trend_gb.html 历年来世界的出生率变化趋势
        2.llh_rate_trend_cn.html 历年来中国的出生率变化趋势
        3.llh_birth.html 中国的生育情况
        4.llh_5_population.html 第五次人口普查
        5.llh_6_population.html 第六次人口普查
        6.llh_adopted_rate 抚养比情况
        7.llh_health.html 老年人健康情况
        8.llh_divorce.html 我国结婚离婚登记情况

base.html /results.html / res1.html / res2.html / res3.html / res4.html / res5.html / res6.html /res7.html /res8.html /
res9.html / res10.html / res12.html / res13.html / res14.html 
* 其中res1到res14分别按顺序对应上面fp与llh文件下的表

### Python档描述
主要使用了flask与pandas模块
* 首先用pandas读取所有数据
* 将选项列表内容按故事1、2用列表分别存入table_available1、table_available2两个变量
* 定义final_run_2019函数，将table_available1、table_available2两个变量的值传给results.html页面
* 定义run_select函数将不同数据赋给对应的data_str变量，并在接下来的if判断中将值传给res变量，通过前端jinjia2内置过滤器{{ the_plot_all|safe }}与{{ the_res|safe }}接收对应图表
* 采用if判断被选选项，打开对应的图，并将图与对应的表格传回相应的页面

### Web App动作描述
1.从主页选择选项-->点击按钮提交-->the_table_selected获取对应的值进行if条件判断-->打开对应的图-->render_templates传回对应网页，plot_all返回对应的图，res返回对应的表
2.从主页进入跳转页-->点击返回按钮-->回到主页

