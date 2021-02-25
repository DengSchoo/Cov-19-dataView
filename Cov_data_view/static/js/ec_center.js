//初始化echarts实例 按照dom去找固定容器 去官网查找设置对应的option
var ec_center = echarts.init(document.getElementById("c2"),"dark"); /*传入dom对象*/
var mydata = [] // 后台获取到的数据 是一个list 值为json格式
var optionMap = { //这里可以从官网下载
		title: {
			text: '',
			subtext: '',
			x: 'left'
		},
		tooltip: {
			trigger: 'item'
		},
		//左侧小导航图标
		visualMap: {
			show: true,
			x: 'left',
			y: 'bottom',
			textStyle: {
				fontSize: 8
			},
			splitList: [ // 数据范围颜色显示
				{start: 1, end: 9},
				{start: 10, end: 99},
				{start: 100, end: 999},
				{start: 1000, end: 9999},
				{start: 10000}
			],
			color: ['#8A3310','#C64918', '#E55B25','#F2AD92', '#F9DCD1']
		},

			//配置属性
			series: [{
				name: '累积确诊人数',
				type: 'map',
				mapType: 'china',
				roam: false, // 禁止缩放
				itemStyle: { // 元素的属性
					normal: {
						borderWidth: .5, // 区域边框宽度
						borderColor: '#009fe8', // 区域边界颜色
						areaColor: '#ffefd5' // 区域颜色
					},
					emphasis: { // 鼠标划过地图高亮
						borderWidth: .5,
						borderColor: '#4b0082',
						areaColor: '#fff'
					}
				},
				label: {
					normal: {
						show: true, //省份名称
						fontSize: 8
					},
					emphasis: {
						show: true,
						fontSize: 8
					}
				},
				data: mydata //数据
			}]
		};

		//使用制定的配置项和数据显示图表
		ec_center.setOption(optionMap);
