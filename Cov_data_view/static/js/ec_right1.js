var ec_right1 = echarts.init(document.getElementById("r1"),"dark");
var color_gol = 'rgb(' +
						Math.round(Math.random() * 255) +
						',' + Math.round(Math.random() * 255) +
						',' + Math.round(Math.random() * 255) + ')';
option_right1 = {
	title: {
		text: '非湖北地区城市确诊TOP7',
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},

	 // grid: {
	 // 	left: 50,
		// top: 50,
	 // 	right: 0,
	 // 	width: '87%',
	 // 	height: 320,
	 // },
	color: color_gol,
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'
		}
	},
	//全局字体样式
	// textStyle: {
	// 	fontFamily: 'PingFangSC-Medium',
	 	fontSize: 12,
	// 	color: '#858E96',
	// 	lineHeight: 12
	// },
	xAxis: {
		type: 'category',
		//                              scale:true,
		data: []
	},
	yAxis: {
		type: 'value',
		//坐标轴刻度设置
		},
	series: [{
		type: 'bar',
		data: [],
		barMaxWidth: "50%",
		showBackground: true,
        backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
        }
	}]
};
ec_right1.setOption(option_right1)
