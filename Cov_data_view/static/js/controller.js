function gettime() {
	$.ajax({
		url: "/time",
		timeout: 10000, //超时时间设置为10秒；
		success: function(data) {
			$("#time").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}
	});

}

function get_c1_data() {
	$.ajax({
		url: "/c1",
		success: function(data) {
			var c1_target = $(".num h1");
			c1_target.eq(0).html(data.confirm); /*num 下 h1标签*/
			c1_target.eq(1).html(data.suspect);
			c1_target.eq(2).html(data.heal);
			c1_target.eq(3).html(data.dead);

		},
		error: function(xhr, type, errorThrown) {

		}
	})
}
function get_c1_update_time() {
	$.ajax({
		url: "/update_time",
		success: function(data) {
			$("#update_time h2").html("最新更新时间:" +data.update_time)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_c2_data() {
	$.ajax({
		url:"/c2",
		success: function(data) {
			optionMap.series[0].data = data.data
			ec_center.setOption(optionMap)
		},
		error: function(xhr, type, errorThrown) {
		
		}
	})
}

function get_l1_data() {
	$.ajax({
		url:"/l1",
		success: function(data) {
			option_left1.xAxis.data = data.day;
			option_left1.series[0].data = data.confirm;
			option_left1.series[1].data = data.suspect;
			option_left1.series[2].data = data.heal;
			option_left1.series[3].data = data.dead;
			ec_left1.setOption(option_left1);
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}



function get_l2_data() {
	$.ajax({
		url:"/l2",
		success: function(data) {
			option_left2.xAxis.data = data.day;
			option_left2.series[0].data = data.confirm_add;
			option_left2.series[1].data = data.suspect_add;
			ec_left2.setOption(option_left2);
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}


function get_r1_data() {
	$.ajax({
		url:"/r1",
		success: function(data) {
			option_right1.xAxis.data = data.city;
			option_right1.series[0].data = data.confirm;
			ec_right1.setOption(option_right1)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}


function get_r2_data() {
	$.ajax({
		url:"/r2",
		success: function(data) {
			option_right2.series[0].data = data.kws;
			ec_right2.setOption(option_right2)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}
function get_recent() {
	$.ajax({
		url:"/recent",
		success: function (data) {
            var elements = $("#group1 a");

			for (var i = 0;i < 20; i++) {
				elements.eq(i).html((i + 1) +'.' + data.title[i]);
				elements.eq(i).attr("href", data.href[i]);
				elements.eq(i).attr("target","_blank");
			}
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_oversea() {
	$.ajax({
		url:"/oversea",
		success: function (data) {
            var elements = $("#group2 a");

			for (var i = 0;i < 20; i++) {
				elements.eq(i).html((i + 1) +'.' + data.title[i]);
				elements.eq(i).attr("href", data.href[i]);
				elements.eq(i).attr("target","_blank");
			}
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_fakes() {
	$.ajax({
		url:"/fakes",
		success: function (data) {
            var elements = $("#group3 a");

			for (var i = 0;i < 20; i++) {
				elements.eq(i).html((i + 1) +'.' + data.title[i]);
				elements.eq(i).attr("href", data.href[i]);
				elements.eq(i).attr("target","_blank");
			}
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}



function set_vis(event) {
	var flags = ["#UI1", "#UI2", "#UI3"];

	for (var i = 0; i < 3; i++) {
		if (event.name == flags[i]) {
			continue;
		}
		$(flags[i]).hide();
	}
		if ($(event.name).is(":visible")) {
			 $(event.name).hide();
		} else {
			$(event.name).show();
		}

}




gettime();
get_c1_data();
get_c2_data();
get_l1_data();
get_l2_data();
get_r1_data();
get_r2_data();
get_recent();
get_fakes();
get_oversea();
get_c1_update_time();
setInterval(gettime, 1000) // 1s执行一次
setInterval(get_c1_data, 1000*10*6);// 10sm执行一次
setInterval(get_c2_data, 1000*10*6);// 10sm执行一次
setInterval(get_l1_data, 1000*10*6);// 10sm执行一次
setInterval(get_l2_data, 1000*10*6);// 10sm执行一次
setInterval(get_r1_data, 1000*10*6);// 10sm执行一次
setInterval(get_r2_data, 1000*10*6);// 10sm执行一次
setInterval(get_recent , 1000*10*6);// 10sm执行一次
setInterval(get_fakes , 1000*10*6);// 10sm执行一次
setInterval(get_oversea , 1000*10*6);// 10sm执行一次
setInterval(get_c1_update_time , 1000*10*6);// 10sm执行一次