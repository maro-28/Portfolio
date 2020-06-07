$(function() {
	var TopBtn = $('#PageTopBtn');
	TopBtn.hide();

	//スクロール中はボタンを非表示
	$(window).on("scroll touchmove", function(){
		TopBtn.stop();
		TopBtn.css('display', 'none');
	});

	//スクロール位置が200でボタンを表示
	$(window).scroll(function() {
		if ($(this).scrollTop() > 200) {
			TopBtn.fadeIn();
		}
		else {
			TopBtn.fadeOut();
		}
	});
	//ボタンを押下するとトップへ移動
	TopBtn.click(function() {
		$('body,html').animate({
			scrollTop: 0
		}, 300);
		return false;
	});
});
