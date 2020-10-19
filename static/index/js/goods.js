// JavaScript Document

function showCartBox(data){
	 ///给某个标签添加html数据然后弹出对话框
	 
	 easyDialog.open({
	  container : "cartBox",
	  autoClose : 2500,
	  fixed : false 
	})
}
/*********属性选择**************/
function spes_select(id,va){
	//document.write(value);
	var attrs = new Object();
	var outattrs = new Object();
	if($(id).parent().attr('class') == 'spec_stop'){//不能点的
		return;
	}
	if($(id).parent().attr('class') == 'spec_active'){
		$(id).parent().removeClass('spec_active');
		var attid=$(id).parent().attr('attrId')//
	    $("#specV_"+attid).attr({value:""});
		/////移除不可点击的可组合的属性
		outattrs=$("#dl_spec"+$(id).parent().attr('otherAttId')).children("dd");
		$.each(outattrs,function (outi, oute){
			if(jQuery.inArray($(oute).attr("attrValue"), spesOutArry[va])<0){
			    if($(oute).attr('class') == 'spec_stop'){
				    $(oute).removeClass('spec_stop');
			    } 
		    }
        });	
	}else{
		/////循环
		attrs=$(id).parent().parent().children("dd");
		$.each(attrs,function (index, dd){
			if($(dd).attr('class') == 'spec_active'){
				$(dd).removeClass('spec_active');
			}
        });	
		/////判断另外一个属性跟当前属性是否是一个组合，否则就显示不可点击
		outattrs=$("#dl_spec"+$(id).parent().attr('otherAttId')).children("dd");
		$.each(outattrs,function (outi, oute){
			if(jQuery.inArray($(oute).attr("attrValue"), spesOutArry[va])>=0){
			    if($(oute).attr('class') == 'spec_stop'){
				    $(oute).removeClass('spec_stop');
			    } 
		    }else{
				$(oute).addClass('spec_stop');
			}
        });	
		//// 
		$(id).parent().addClass('spec_active');
		var attid=$(id).parent().attr('attrId')//
	    $("#specV_"+attid).attr({value:va,specValue:spesArry[va]});
		
	}
	showMsgBox();
}
/************显示目前已经选择或者的属性************/
$(function(){
	showMsgBox();
	
	
})
///显示选中属性的对话框
function showMsgBox(){
	var specInput=new Object();
	var str="";
	var goodsSelect="";//用来判断已经选中的产品sku
	specInput=$("#input_spec").children('input');
	if(specInput.size()>0){
		$.each(specInput,function(index,element){ //遍历数组
		  if($(element).attr("value")){///判断是否 有属性被选中
			  if(index==0){
				  str=$(element).attr('specCatName')+":"+$(element).attr('specValue');
				  //goodsSelect=$(element).attr("value");
			  }else{
				  str+=" "+$(element).attr('specCatName')+":"+$(element).attr('specValue');
			  }
			  goodsSelect+=+$(element).attr("value");//sku字符串
		  }
	    })
		///赋值给标签显示内容
		if(str){
			 $("#spec_msg_box").show();
		     $("#spec_msg_box").html("你已选择【"+"<span>"+str+"</span>】");
			 if(goods[goodsSelect]){
			     $("#sku").html("商品规格："+goods[goodsSelect].sku)
				 ////动态获取数量和价格
				 $.ajax({
					 type: "post",
					 dataType :"json",
					 url: "goods.php",
					 data: "act=price_storage&sku="+goods[goodsSelect]['sku'],
					 success: function(msg){
					   $("#price").html("现价："+msg.price)
					   panBuanNumber(msg.product_number)
					 }
				  });
			 }else{
				 $("#sku").html("商品编码："+goods['goods_sn'])
				 $("#price").html("现价："+goods['sectionPrice'])
				 //$("#storages").html("(库存："+goodsNumber+")")
				 panBuanNumber(goodsNumber)
			 }
		}else{
			 $("#spec_msg_box").hide();
			 $("#sku").html("商品编码："+goods['goods_sn'])
			 $("#price").html("现价："+goods['sectionPrice'])
			 ///
			 panBuanNumber(msg.product_number)
			 
		}
	}
}
/****判断属性是否选择好买或者是库存为零****/
function judgment(){//判断是否所有属性都被选择了
	var specInput=new Object();
	var returnArray=new Array();
	var strName=""
	var strID=""
	specInput=$("#input_spec").children('input');
	if(specInput.size()>0){
		var i=0;
		$.each(specInput,function(index,element){ //遍历数组
		  if(!$(element).attr("value")){///判断是否 有属性被选中
			/*returnArray[i]=$(element).attr("specCatName");
			i++;*/
			if(i>0){
				 strName+="、"+$(element).attr("specCatName");
			}else{
				 strName+=$(element).attr("specCatName");
			}
			i++;
		  }else{
			  strID+=$(element).attr("value");
		  }
	    })
	}
	returnArray['strName']=strName;
	returnArray['strID']=strID;
	/////
	return returnArray;
}