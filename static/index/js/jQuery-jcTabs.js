/*
 * jQuery - jcTabs v1.10
 * Copyright(c) 2012 by Riddick-design 
 * Date: 2012-02-04
 * 相关参数: 
   visitedClass:'visited',  // 点击后样式定义类
   tabsEvent:'click',   // tabs执行效果，如click,mouseover等
   tabsScorll:true,         // tabs滑动模式，true启动内容滑动模式
   sliderBtn:true,          // tabs滑动模式下是否需要左右按钮
   BtnOffsetX:-30,          // tabs滑动模式下按钮水平偏移
   BtnOffsetY:0,            // tabs滑动模式下按钮垂直偏移
   speed:'easeInOutExpo',   // tabs滑动模式下内容滑动速度
   indexDefaults:0          // 设置tabs开始的初始值
 */
;(function($){
	$.fn.jcTabs = function(options) {
		var defaults = {
			visitedClass:'visited', 
			tabsEvent:'click',
			tabsScorll:true,
			sliderBtn:true,
			BtnOffsetX:-30,
			BtnOffsetY:0,
			speed:'easeInOutExpo',
			indexDefaults:0
		};
		var options = $.extend(defaults,options);
		return this.each(function() {
			var $thisTabs = $(this),
			    thisIndex = 0,
			    $tabsContent = $thisTabs.children('div'),
				$tabs = $thisTabs.children('ul');
		    if(options.tabsScorll){
				$tabsContent.wrap("<span id='wrap'>"+"</span>");
				var $wrap = $('#wrap'),
				    $wrapContent = $wrap.children('div'),
			    	_Rclass = $wrapContent.attr('class');
				$wrap.css({ "clear":"both",
						    "display":"block",
						    "overflow":"hidden",
						    "position":"relative" });
				_wrapWidth = $wrap.width();
				_wrapHeight = $wrap.height();
				_tabsHeight = $tabs.height();
				$wrapContent.removeClass(_Rclass)
				            .addClass('wrapContent')
							.css({ "position":"absolute",
								   "left":0,
								   "top":0,
								   "z-index":998,
								   "width":"9999%",
								   "height":200 })
							.find('div')
							.css('float','left');
		    } else {
				$tabsContent.children('*').hide().eq(options.indexDefaults-1).show();
			};
			$tabs.find('li')
			     .eq(options.indexDefaults-1)
				 .addClass(options.visitedClass)
				 .end()
				 .bind(options.tabsEvent,function(){
					 $tabs.find('li').removeClass(options.visitedClass);
					 $(this).addClass(options.visitedClass);
					 var $index = $tabs.find('li').index($(this));
                     if(options.tabsScorll){
                     	$wrapContent.stop().animate({left:-($index*_wrapWidth)},options.speed)
                     } else {
                     	$tabsContent.children('div').hide().eq($index).show();
                     };
					 thisIndex = $index
					 return false;
				 });
			if(options.sliderBtn && options.tabsScorll){
				$thisTabs.append("<a class='prev'></a><a class='next'></a>");
				function BtnAnimate(Index,Wwidth){
					$tabs.find('li').removeClass(options.visitedClass);
					$tabs.find('li').eq(Index).addClass(options.visitedClass);
					$wrapContent.stop().animate({left:-Index*Wwidth},options.speed);
					return false;
				};
				$('a.prev').css({ 'top':(_wrapHeight-$('.prev').height())/2+_tabsHeight+options.BtnOffsetY,
								  'left': options.BtnOffsetX })
						   .click(function(){
							    if(thisIndex>0){
								    thisIndex = thisIndex-1;
								} else {
									thisIndex = $tabs.find('li').size()-1;
								};
								BtnAnimate(thisIndex,_wrapWidth);
								return false;
							});
				$('a.next').css({ 'top':(_wrapHeight-$('.next').height())/2+_tabsHeight+options.BtnOffsetY,
								  'left':_wrapWidth-$('.next').width()-options.BtnOffsetX })
						   .click(function(){
							    if(thisIndex<$tabs.find('li').size()-1){
								    thisIndex = thisIndex+1;
								} else {
									thisIndex = 0;
								};
								BtnAnimate(thisIndex,_wrapWidth);
								return false;
							});
			};
		});
	};
})(jQuery)