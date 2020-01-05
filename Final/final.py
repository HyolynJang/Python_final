
from flask import Flask, render_template, request
import pandas as pd



app = Flask(__name__)

# 准备工作

#读取故事1扶贫的所有数据
df1 = pd.read_csv('./static/data/fp/gdp.csv', encoding='utf-8-sig', sep=',')
df2 = pd.read_csv('./static/data/fp/city_rural_income.csv', encoding='utf-8-sig', sep=',')
df3 = pd.read_csv('./static/data/fp/province_gdp.csv', encoding='utf-8-sig', sep=',')
df4 = pd.read_csv('./static/data/fp/rural_security.csv',encoding='utf-8-sig', sep=',')
df5 = pd.read_csv('./static/data/fp/city_security.csv')
df6 = pd.read_csv('./static/data/fp/employed.csv', encoding='utf-8',sep=',')


#读取故事2老龄化的所有数据
df7 = pd.read_csv('./static/data/llh/llh_birth_rate_gb.csv', encoding='utf-8-sig', sep=',')
df8 = pd.read_csv('./static/data/llh/llh_birth_rate_cn.csv', encoding='utf-8-sig', sep=',')
df9 = pd.read_csv('./static/data/llh/llh_birth_cn.csv', encoding='utf-8-sig', sep=',')
df10 = pd.read_excel('./static/data/llh/5_population_sex_rate.xlsx')
df11 = pd.read_csv('./static/data/llh/6_population_sex_rate.csv')
df12 = pd.read_csv('./static/data/llh/llh_adopted_rate.csv', encoding='utf-8',sep=',')
df13 = pd.read_csv('./static/data/llh/llh_health.csv', encoding='utf-8',sep=',')
df14 = pd.read_csv('./static/data/llh/llh_married.csv', encoding='utf-8',sep=',')

table_available1=['GDP、农村城市低保的对比','城镇农村人均可支配收入','2011年分省GDP',
                 '历年中国各省农村最低生活保障人数','历年中国各省城市最低生活保障人数','城乡就业人员的变化']

table_available2=['历年来世界的出生率变化趋势','历年来中国的出生率变化趋势','中国的生育情况','人口老龄化现状','抚养比情况','老年人健康情况','我国结婚离婚登记情况']


@app.route('/',methods=['GET'])
def final_run_2019():
    """enter the homepage and reture the available value"""
    return render_template('results.html',
                           the_select_table1=table_available1,
                           the_select_table2=table_available2,
                           )

@app.route('/entry',methods=['POST'])
def run_select() -> 'html':

    # 故事1
    data_str1 = df1.to_html()
    data_str2 = df2.to_html()
    data_str3 = df3.to_html()
    data_str4 = df4.to_html()
    data_str5 = df5.to_html()
    data_str6 = df6.to_html()
    # 故事2
    data_str7 = df7.to_html()
    data_str8 = df8.to_html()
    data_str9 = df9.to_html()
    data_str10 = df10.to_html()
    data_str11 = df11.to_html()
    data_str12 = df12.to_html()
    data_str13 = df13.to_html()
    data_str14 = df14.to_html()

    the_table_selected= request.form["the_table_selected"]
    if the_table_selected=="GDP、农村城市低保的对比":
        with open("./templates/fp/fp_dbcomparison.html", encoding="utf8", mode="r") as f:
            plot_all1 = "".join(f.readlines())
        return render_template('res1.html',the_plot_all1=plot_all1,the_res1=data_str1,the_res4=data_str4,the_res5=data_str5)
    elif the_table_selected=="城镇农村人均可支配收入":
        with open("./templates/fp/fp_czkzp.html", encoding="utf8", mode="r") as f:
            plot_all2 = "".join(f.readlines())
        return render_template('res2.html',the_plot_all2=plot_all2,the_res2=data_str2)
    elif the_table_selected=="2011年分省GDP":
        with open("./templates/fp/fp_gdp.html", encoding="utf8", mode="r") as f:
            plot_all3 = "".join(f.readlines())
        return render_template('res3.html', the_plot_all3=plot_all3,the_res3=data_str3)
    elif the_table_selected=="历年中国各省农村最低生活保障人数":
        with open("./templates/fp/fp_rural_security.html", encoding="utf8", mode="r") as f:
            plot_all4 = "".join(f.readlines())
        return render_template('res4.html', the_plot_all4=plot_all4,the_res4=data_str4)
    elif the_table_selected=="历年中国各省城市最低生活保障人数":
        with open("./templates/fp/fp_city_security.html", encoding="utf8", mode="r") as f:
            plot_all5 = "".join(f.readlines())
        return render_template('res5.html', the_plot_all5=plot_all5,the_res5=data_str5)
    elif the_table_selected == "城乡就业人员的变化":
        with open("./templates/fp/fp_job_trend.html", encoding="utf8", mode="r") as f:
            plot_all6 = "".join(f.readlines())
        return render_template('res6.html', the_plot_all6=plot_all6,the_res6=data_str6)
    elif the_table_selected == "历年来世界的出生率变化趋势":
        with open("./templates/llh/llh_rate_trend_gb.html", encoding="utf8", mode="r") as f:
            plot_all7 = "".join(f.readlines())
        return render_template('res7.html', the_plot_all7=plot_all7,the_res7=data_str7)
    elif the_table_selected == "历年来中国的出生率变化趋势":
        with open("./templates/llh/llh_rate_trend_cn.html", encoding="utf8", mode="r") as f:
            plot_all8 = "".join(f.readlines())
        return render_template('res8.html', the_plot_all8=plot_all8,the_res8=data_str8)
    elif the_table_selected == "中国的生育情况":
        with open("./templates/llh/llh_birth.html", encoding="utf8", mode="r") as f:
            plot_all9 = "".join(f.readlines())
        return render_template('res9.html', the_plot_all9=plot_all9,the_res9=data_str9)
    elif the_table_selected == "人口老龄化现状":
        with open("./templates/llh/llh_5_population.html", encoding="utf8", mode="r") as f:
            plot_all10 = "".join(f.readlines())
        with open("./templates/llh/llh_6_population.html", encoding="utf8", mode="r") as f:
            plot_all11 = "".join(f.readlines())
        return render_template('res10.html', the_plot_all10=plot_all10,the_plot_all11=plot_all11,the_res10=data_str10,the_res11=data_str11)
    elif the_table_selected == "抚养比情况":
        with open("./templates/llh/llh_adopted_rate.html", encoding="utf8", mode="r") as f:
            plot_all12 = "".join(f.readlines())
        return render_template('res12.html', the_plot_all12=plot_all12,the_res12=data_str12 )
    elif the_table_selected=="老年人健康情况":
        with open("./templates/llh/llh_health.html", encoding="utf8", mode="r") as f:
            plot_all13 = "".join(f.readlines())
        return render_template('res13.html', the_plot_all13=plot_all13,the_res13=data_str13)

    else:
        with open("./templates/llh/llh_divorce.html", encoding="utf8", mode="r") as f:
            plot_all14 = "".join(f.readlines())
        return render_template('res14.html', the_plot_all14=plot_all14, the_res14=data_str14)



if __name__ == '__main__':
    app.run(debug=True,port=8000)
