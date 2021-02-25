let scale = 1;
let echartData = [];
let rich = {
    yellow: {
        color: "#ffc72b",
        fontSize: 30 * scale,
        padding: [5, 4],
        align: 'center'
    },
    total: {
        color: "#ffc72b",
        fontSize: 40 * scale,
        align: 'center'
    },
    white: {
        color: "#fff",
        align: 'center',
        fontSize: 14 * scale,
        padding: [21, 0]
          },
    blue: {
        color: '#49dff0',
        fontSize: 16 * scale,
        align: 'center'
    },
    hr: {
        borderColor: '#0b5263',
        width: '100%',
        borderWidth: 1,
        height: 0,
    }
};
    let option = {
      title: {
        text:'总考生数',
        left:'center',
        top:'53%',
        padding:[24,0],
        textStyle:{
          color:'#fff',
          fontSize:18*scale,
          align:'center'
        }
      },
      legend: {
        selectedMode:false,
        formatter: function(name) {
          let total = 0; //各科正确率总和
          let averagePercent; //综合正确率
          echartData.forEach(function(value, index, array) {
            total += value.value;
          });
          return '{total|' + total + '}';
        },
        data: [echartData[0].name],
        // data: ['高等教育学'],
        // itemGap: 50,
        left: 'center',
        top: 'center',
        icon: 'none',
        align:'center',
        textStyle: {
          color: "#fff",
          fontSize: 16 * scale,
          rich: rich
        },
      },
      series: [{
        name: '总考生数量',
        type: 'pie',
        radius: ['42%', '50%'],
        hoverAnimation: false,
        color: function() { //文字颜色的随机色
                // return 'rgb(' + [
                // 	Math.round(Math.random() * 250),
                // 	Math.round(Math.random() * 250),
                // 	Math.round(Math.random() * 250)
                // ].join(',') + ')';
                return 'rgb(' +
                    Math.round(Math.random() * 255) +
                    ',' + Math.round(Math.random() * 255) +
                    ',' + Math.round(Math.random() * 255) + ')'
            },
        label: {
          textStyle: {
            fontSize: 12
          },
          normal: {
            formatter: function(params, ticket, callback) {
              let total = 0; //考生总数量
              let percent = 0; //考生占比
              echartData.forEach(function(value, index, array) {
                total += value.value;
              });
              percent = ((params.value / total) * 100).toFixed(1);
              return '{white|' + params.name + '}\n{hr|}\n{yellow|' + params.value + '}\n{blue|' + percent + '%}';
            },
            rich: rich
          },
        },
        labelLine: {
          normal: {
            length: 55 * scale,
            length2: 0,
            lineStyle: {
              color: '#0b5263'
            }
          }
        },
        data: echartData
      }]
    };
    chart.setOption(option, true);
