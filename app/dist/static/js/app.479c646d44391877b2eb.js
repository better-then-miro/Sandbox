webpackJsonp([1],{"6Wod":function(t,e){},BrRs:function(t,e){},NHnr:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i("7+uW"),a=i("Gu7T"),o=i.n(a),s=i("85RH"),r=i.n(s),l=i("fZjL"),c=i.n(l),d=i("Zrlr"),h=i.n(d),u=function t(e,i,n,a){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:"free",s=arguments.length>5&&void 0!==arguments[5]?arguments[5]:[],r=arguments.length>6&&void 0!==arguments[6]?arguments[6]:[];h()(this,t),this.Id=null,this.name="",this.description="",this.Type="",this.mode="",this.blocks=[],this.links=[],this.Id=e,Object.defineProperty(this,"Id",{writable:!1}),this.name=i,this.description=n,this.Type=a,this.mode=o,this.blocks=s,this.links=r},p=function t(e,i,n){var a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:[];h()(this,t),this.Id=null,this.name="",this.description="",this.diagrams=[],this.name=i,this.description=n,this.Id=e,Object.defineProperty(this,"Id",{writable:!1}),this.diagrams=a},g=i("mtWM");function m(t){var e={Id:t.Id,width:t.width,height:t.height,coords:t.coords,title:t.title,description:t.description,additionalFields:t.additionalFields};console.log("Properties to update: ",e),g.post("http://127.0.0.1:5000/updateBlockProperties",e).then(function(t){return console.log(t)})}var v={x1:0,y1:0,x2:0,y2:0},k=function(t,e,i,n){if(!1===this.data("blockView").isScaling){if(i>=v.x1&&n>=v.y1&&i<=v.x2&&n<=v.y2){this.attr({transform:this.data("ot")+(this.data("ot")?"T":"t")+[t,e]});for(var a=this.data("blockView").connections.length;a--;)this.data("blockView").snap.connection(this.data("blockView").connections[a])}(Math.abs(t)>2||Math.abs(e)>2)&&this.data("saveDrag",!0)}},f=function(){this.data("ot",this.transform().local),this.data("saveDrag",!1)},w=function(){if(!1!==this.data("saveDrag")){c()(this.data("blockView").block.additionalFields).length>0&&this[2].remove();var t=this.getBBox(),e=[];e="Use-case"===this.data("blockView").block.Type?[Math.round(t.cx),Math.round(t.cy)]:[Math.round(t.x),Math.round(t.y)],this.data("blockView").block.setCoords(e),m(this.data("blockView").block),this.data("blockView").redrawOnSnap()}},b=null,y=null,_=1,I=1,x=function(){b.data("origTransform",b.transform().local)},D=function(t,e){var i=b.getBBox(),n=1,a=1;"topleft"===this.data("side")?(n=t>0?i.width/(i.width+t):(i.width-t)/i.width,a=e>0?i.height/(i.height+e):(i.height-e)/i.height):"topright"===this.data("side")?(n=t>0?(i.width+t)/i.width:i.width/(i.width-t),a=e>0?i.height/(i.height+e):(i.height-e)/i.height):"bottomleft"===this.data("side")?(n=t>0?i.width/(i.width+t):(i.width-t)/i.width,a=e>0?(i.height+e)/i.height:i.height/(i.height-e)):"bottomright"===this.data("side")&&(n=t>0?(i.width+t)/i.width:i.width/(i.width-t),a=e>0?(i.height+e)/i.height:i.height/(i.height-e)),b[0].getBBox().width*n>100&&(_=n),b[0].getBBox().height*a>50&&(I=a),b.attr({transform:b.data("origTransform")+(b.data("origTransform")?"S":"s")+_+","+I})},C=function(){};function B(t){b[0].remove();var e=b.getBBox();"Use-case"===t.data("blockView").block.Type?t.data("blockView").block.setCoords([Math.round(e.cx),Math.round(e.cy)]):t.data("blockView").block.setCoords([Math.round(e.x),Math.round(e.y)]),t.data("blockView").block.setWidth(Math.round(e.width)),t.data("blockView").block.setHeight(Math.round(e.height)),t.data("blockView").isScaling=!1,m(t.data("blockView").block),t.data("blockView").redrawOnSnap(),b.remove(),y=null}var T=function(){var t=this.data("blockView").snap;if(null!=y&&y!==this&&B(y),y=this,!1===this.data("blockView").isScaling){this.data("blockView").isScaling=!0;var e=this[0].getBBox(),i=[];i[0]=t.circle(e.x,e.y,5).attr({class:"handler",fill:"blue"}),i[0].data("side","topleft"),i[0].drag(D,x,C),i[1]=t.circle(e.x+e.width,e.y,5).attr({class:"handler",fill:"blue"}),i[1].data("side","topright"),i[1].drag(D,x,C),i[2]=t.circle(e.x,e.y+e.height,5).attr({class:"handler",fill:"blue"}),i[2].data("side","bottomleft"),i[2].drag(D,x,C),i[3]=t.circle(e.x+e.width,e.y+e.height,5).attr({class:"handler",fill:"blue"}),i[3].data("side","bottomright"),i[3].drag(D,x,C),b=t.group(this,i[0],i[1],i[2],i[3])}else B(this)},j=null,M=function(){j=this.data("blockView")},N=i("wxAW"),P=i.n(N),S=i("W3Iv"),F=i.n(S),A=i("BO1k"),V=i.n(A),L=i("d7EF"),E=i.n(L),U=i("daKz"),G=i.n(U),$=function(){function t(e){h()(this,t),this.snap=null,this.snap=e}return P()(t,[{key:"svgCreate_byType",value:function(t,e,i,n,a){return"Class"===t?this.svgCreate_ClassBlock(e,i,n,a):"Use-case"===t?this.svgCreate_UseCase(e,i,n,a):"Actor"===t?this.svgCreate_Actor(e,i,n,a):null}},{key:"svgCreate_ClassBlock",value:function(t,e,i,n){var a=this.snap.rect(t,e,i,n);return a.attr({fill:"#60efff",stroke:"black",strokeWidth:1}),a}},{key:"svgCreate_UseCase",value:function(t,e,i,n){var a=Math.round(i/2),o=Math.round(n/2),s=this.snap.ellipse(t+a,e+o,a,o);return s.attr({fill:"#60efff",stroke:"black",strokeWidth:1}),s}},{key:"svgCreate_UseCaseCenter",value:function(t,e,i,n){var a=this.snap.ellipse(t,e,i,n);return a.attr({fill:"#60efff",stroke:"black",strokeWidth:1}),a}},{key:"svgCreate_Actor",value:function(t,e,i,n){var a=this.snap.group();return a.data("ot",a.transform().local),r.a.load(G.a,function(t){console.log(t),a.append(t)}),a.attr({transform:a.data("ot")+(a.data("ot")?"T":"t")+[t,e]}),a}},{key:"svgCreate_BlockFields",value:function(t,e,i,n,a){var o=15,s=this.snap.group();s.attr({"font-size":"13px"});var r=!0,l=!1,c=void 0;try{for(var d,h=V()(F()(a));!(r=(d=h.next()).done);r=!0){var u=d.value,p=E()(u,2),g=p[0],m=p[1];if(0!==m.length){var v=this.snap.text(t+Math.round(i/2),e+n+o,g).attr({stroke:"black",dominantBaseline:"middle",textAnchor:"middle"});for(var k in o+=20,s.append(v),m){var f=this.snap.text(t+Math.round(i/2),e+n+o,m[k]).attr({dominantBaseline:"start",textAnchor:"middle"});o+=15,s.append(f)}o+=10}}}catch(t){l=!0,c=t}finally{try{!r&&h.return&&h.return()}finally{if(l)throw c}}return s}}]),t}(),z=function(){function t(e,i,n){h()(this,t),this.block=null,this.connections=null,this.isScaling=!1,this.snap=null,this.factory=null,this.blockGroup=null,this.block=e,this.snap=i,this.connections=n,this.factory=new $(i)}return P()(t,[{key:"redrawOnSnap",value:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:this.block.coords[0],e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:this.block.coords[1],i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:this.block.width,n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:this.block.height;if(null!=this.blockGroup&&this.blockGroup.remove(),this.blockGroup=this.snap.group(),"Class"===this.block.Type){var a=this.factory.svgCreate_ClassBlock(t,e,i,n),o=this.factory.svgCreate_BlockFields(t,e,i,n,this.block.additionalFields),s=this.snap.text(t+Math.round(i/2),e+Math.round(n/2),this.block.title).attr({stroke:"black",dominantBaseline:"middle",textAnchor:"middle"});this.blockGroup.add(a,s,o)}else if("Use-case"===this.block.Type){var r=this.factory.svgCreate_UseCaseCenter(t,e,Math.round(i/2),Math.round(n/2)),l=this.snap.text(t,e,this.block.title).attr({stroke:"black",dominantBaseline:"middle",textAnchor:"middle"});this.blockGroup.add(r,l)}else if("Actor"===this.block.Type){var c=this.factory.svgCreate_Actor(t,e,Math.round(i/2),Math.round(n/2)),d=this.snap.text(t+Math.round(i/2),e+n,this.block.title).attr({stroke:"black",dominantBaseline:"middle",textAnchor:"middle"});this.blockGroup.add(c,d)}for(var h=this.connections.length;h--;)this.snap.connection(this.connections[h]);this.blockGroup.drag(k,f,w),this.blockGroup.dblclick(T),this.blockGroup.click(M),this.blockGroup.data("blockView",this)}}]),t}();r.a.plugin(function(t,e){e.prototype.connection=function(t,e,i,n){t.line&&t.from&&t.to&&(t=(i=t).from,e=i.to);for(var a=t.blockGroup.getBBox(),o=e.blockGroup.getBBox(),s=[{x:a.x+a.width/2,y:a.y-1},{x:a.x+a.width/2,y:a.y+a.height+1},{x:a.x-1,y:a.y+a.height/2},{x:a.x+a.width+1,y:a.y+a.height/2},{x:o.x+o.width/2,y:o.y-1},{x:o.x+o.width/2,y:o.y+o.height+1},{x:o.x-1,y:o.y+o.height/2},{x:o.x+o.width+1,y:o.y+o.height/2}],r={},l=[],c=0,d=0,h=void 0,u=0;u<4;u+=1)for(var p=4;p<8;p+=1)c=Math.abs(s[u].x-s[p].x),d=Math.abs(s[u].y-s[p].y),(u===p-4||(3!==u&&6!==p||s[u].x<s[p].x)&&(2!==u&&7!==p||s[u].x>s[p].x)&&(0!==u&&5!==p||s[u].y>s[p].y)&&(1!==u&&4!==p||s[u].y<s[p].y))&&(l.push(c+d),r[l[l.length-1]]=[u,p]);var g=s[(h=0===l.length?[0,4]:r[Math.min.apply(Math,l)])[0]].x,m=s[h[0]].y,v=s[h[1]].x,k=s[h[1]].y;c=Math.max(Math.abs(g-v)/2,10),d=Math.max(Math.abs(m-k)/2,10);var f=[g,g,g-c,g+c][h[0]].toFixed(3),w=[m-d,m+d,m,m][h[0]].toFixed(3),b=[0,0,0,0,v,v,v-c,v+c][h[1]].toFixed(3),y=[0,0,0,0,m+d,m-d,k,k][h[1]].toFixed(3),_=["M"+g.toFixed(3),m.toFixed(3)+"C"+f,w,b,y,v.toFixed(3),k.toFixed(3)].join(",");if(!i||!i.line){var I="string"==typeof i?i:"#000";return{bg:n&&n.split&&this.path(_).attr({stroke:n.split("|")[0],fill:"none","stroke-width":n.split("|")[1]||3}),line:this.path(_).attr({stroke:I,fill:"none"}),from:t,to:e}}i.bg.attr({path:_}),i.line.attr({path:_})}});var O={name:"DiagramUi",props:{currentDiagram:u},emits:{"ready-add-new-link":{sourceID:Number,targetID:Number},"block-view-selected":z},data:function(){return{snap:null,selectedBlockView:null,snapBlocks:[],snapLinks:[],linkSourceBlock:null,isLinkAddMode:!1}},mounted:function(){this.snap=r()("#mySvg"),this.init()},methods:{init:function(){var t=this;v={x1:10,y1:10,x2:710,y2:710},this.snap.attr({viewBox:"0 0 700 700"}),this.snap.rect(0,0,700,700).attr({fill:"none",stroke:"black"}),this.currentDiagram.blocks.forEach(function(e){var i=new z(e,t.snap,t.snapLinks);i.redrawOnSnap(),t.snapBlocks.push(i)}),this.currentDiagram.links.forEach(function(e){var i=t.snapBlocks.filter(function(t){return t.block.Id===e.sId}),n=t.snapBlocks.filter(function(t){return t.block.Id===e.tId});1===i.length&&1===n.length?t.snapLinks.push(t.snap.connection(i[0],n[0],"#333","#111")):console.log("Incorrect link parameters!")})},drawNewBlock:function(t){var e=new z(t,this.snap,this.snapLinks);e.redrawOnSnap(),this.snapBlocks.push(e)},updateInfo:function(){this.selectedBlockView=j,this.$emit("block-view-selected",this.selectedBlockView),this.isLinkAddMode?null!=this.linkSourceBlock&&this.linkSourceBlock.block.Id!==j.block.Id?this.$emit("ready-add-new-link",{sourceID:this.linkSourceBlock.block.Id,targetID:j.block.Id}):this.linkSourceBlock=j:this.linkSourceBlock=null},drawNewLink:function(){console.log("Drawing new link"),null!=j&&null!=this.linkSourceBlock?(this.snapLinks.push(this.snap.connection(this.linkSourceBlock,j,"#333","#111")),this.linkSourceBlock=null,this.isLinkAddMode=!1):console.log("Error drawing new link")},toggleLinkMode:function(t){this.isLinkAddMode=t.bool},changeFields:function(){this.selectedBlockView.redrawOnSnap()}}},W={render:function(){var t=this.$createElement;return(this._self._c||t)("svg",{staticClass:"editorSvg",attrs:{id:"mySvg",height:"700",width:"700"},on:{click:this.updateInfo}})},staticRenderFns:[]};var Z=i("VU/8")(O,W,!1,function(t){i("BrRs")},"data-v-b90dd8e4",null).exports,H={name:"SelectionEntry",props:{blockType:String,selectedEntry:String},emits:{"entry-selected":null},data:function(){return{snap:null,factory:null}},mounted:function(){this.snap=r()("#svgID_"+this.blockType),this.snap.attr({viewBox:"0 0 80 80"}),this.factory=new $(this.snap),this.factory.svgCreate_byType(this.blockType,0,0,80,80)},methods:{select:function(){console.log("Entry selected: ",this.blockType),this.$emit("entry-selected",this.blockType)}},computed:{isSelected:function(){return this.blockType===this.selectedEntry}}},R={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"selection-entry",class:{selected:this.isSelected},staticStyle:{display:"flex","flex-direction":"column"},on:{click:this.select}},[e("svg",{staticClass:"blockSvg",attrs:{id:"svgID_"+this.blockType,height:"60",width:"60"}}),this._v("\n  "+this._s(this.blockType)+"\n")])},staticRenderFns:[]};var X={name:"SidePanel",components:{SelectionEntry:i("VU/8")(H,R,!1,function(t){i("6Wod")},"data-v-5976a018",null).exports},props:{isLinkAddMode:Boolean,supportedBlockTypes:Array},emits:{"toggle-link-mode":{bool:Boolean},"create-block":{Type:String,title:String}},data:function(){return{blockTitle:"",blockType:null,linkType:null}},methods:{addNewBlock:function(){if(null!=this.blockType){var t=void 0;t=""===this.blockTitle.replaceAll(" ","")?this.blockType:this.blockTitle,this.$emit("create-block",{Type:this.blockType,title:t}),this.clear()}},toggleLinkMode:function(){this.$emit("toggle-link-mode",{bool:!this.isLinkAddMode})},clear:function(){this.blockTitle="",this.blockType=null,this.linkType=null},changeSelected:function(t){this.blockType=t}}},Y={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.blockTitle,expression:"blockTitle"}],attrs:{id:"blockTitle",type:"text",placeholder:"Enter block title",name:"blockTitle"},domProps:{value:t.blockTitle},on:{input:function(e){e.target.composing||(t.blockTitle=e.target.value)}}}),t._v(" "),i("div",{staticClass:"selection-grid",staticStyle:{display:"flex","flex-direction":"row"}},[t._l(t.supportedBlockTypes,function(e){return i("selection-entry",{key:e,attrs:{"block-type":e,"selected-entry":t.blockType},on:{"entry-selected":t.changeSelected}})}),t._v(" "),i("button",{staticClass:"btn icon-plus sidePanelBtn",attrs:{type:"button"},on:{click:function(e){return t.addNewBlock()}}},[t._v("\n      Add new block\n    ")])],2),t._v(" "),i("div",{staticStyle:{display:"flex","flex-direction":"column","justify-content":"space-around","align-items":"center"}},[i("div",{staticStyle:{display:"flex","flex-direction":"row","justify-content":"space-around","align-items":"center"}},[i("div",{staticStyle:{margin:"5px"}},[i("input",{directives:[{name:"model",rawName:"v-model",value:t.linkType,expression:"linkType"}],attrs:{type:"radio",id:"linkChoice1",name:"linkType",value:"Association"},domProps:{checked:t._q(t.linkType,"Association")},on:{change:function(e){t.linkType="Association"}}}),t._v(" "),i("label",{attrs:{for:"linkChoice1"}},[t._v("Association")])]),t._v(" "),i("div",{staticStyle:{margin:"5px"}},[i("input",{directives:[{name:"model",rawName:"v-model",value:t.linkType,expression:"linkType"}],attrs:{type:"radio",id:"linkChoice2",name:"linkType",value:"Include"},domProps:{checked:t._q(t.linkType,"Include")},on:{change:function(e){t.linkType="Include"}}}),t._v(" "),i("label",{attrs:{for:"linkChoice2"}},[t._v("Include")])]),t._v(" "),i("button",{staticClass:"btn icon-plus sidePanelBtn",attrs:{type:"button"},on:{click:function(e){return t.toggleLinkMode()}}},[t._v("\n        Toggle link mode\n      ")])]),t._v(" "),t.isLinkAddMode?i("h3",{staticStyle:{margin:"5px"}},[t._v("Link mode")]):t._e()])])},staticRenderFns:[]};var q=i("VU/8")(X,Y,!1,function(t){i("PvSH")},"data-v-cd86eed8",null).exports,J={name:"EditingPanel",props:{selectedBlockView:z},emits:{"close-panel":null,"apply-changes":{additionalFields:{},title:String,description:String},"item-deleted":{}},data:function(){return{snap:null}},methods:{close:function(){this.$emit("close-panel")},apply:function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0],e={},i=c()(this.selectedBlockView.block.additionalFields);for(var n in i)e[i[n]]=[];this.$refs.additionalFieldsSection.querySelectorAll("input").forEach(function(i){i.id in e==!1&&(e[i.id]=[]),(t||""!==i.value)&&e[i.id].push(i.value)}),this.selectedBlockView.blockGroup[1].node.textContent=this.$refs.blockTitle.value,this.$emit("apply-changes",{additionalFields:e,title:this.$refs.blockTitle.value,description:this.$refs.blockDescription.value})},addNewItem:function(t){this.apply(!0);var e=!0;this.$refs.additionalFieldsSection.querySelectorAll("input").forEach(function(i){i.id===t&&""===i.value&&(e=!1)}),e&&(t in this.selectedBlockView.block.additionalFields==!1&&(this.selectedBlockView.block.additionalFields[t]=[]),this.selectedBlockView.block.additionalFields[t].push(""))},deleteItem:function(t,e){var i={};this.$refs.additionalFieldsSection.querySelectorAll("input").forEach(function(n){n.id in i==!1&&(i[n.id]=[]),!1==(n.id===t&&n.value===e)&&i[n.id].push(n.value)}),this.$emit("item-deleted",i)}}},K={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"editing-panel"},[i("div",{staticClass:"panel-header"},[i("h2",[t._v("Block modification")]),t._v(" "),i("span",{staticClass:"closeForm",attrs:{title:"Close panel"},on:{click:t.close}},[t._v("X")])]),t._v(" "),i("h3",{staticClass:"input-title",staticStyle:{"margin-top":"5px","margin-bottom":"5px"}},[t._v("\n      Name:\n  ")]),t._v(" "),i("input",{ref:"blockTitle",staticStyle:{padding:"15px","padding-top":"5px","margin-bottom":"5px","font-size":"17px"},attrs:{id:"selectedBlockTitle",type:"text",placeholder:"Enter block title",name:"blockTitle"},domProps:{value:t.selectedBlockView.block.title}}),t._v(" "),i("h3",{staticClass:"input-title",staticStyle:{"margin-top":"5px","margin-bottom":"5px"}},[t._v("\n      Description:\n  ")]),t._v(" "),i("input",{ref:"blockDescription",staticStyle:{padding:"15px","padding-top":"5px","margin-bottom":"5px","font-size":"17px"},attrs:{id:"selectedBlockDescription",type:"text",placeholder:"Enter block description",name:"blockDescription"},domProps:{value:t.selectedBlockView.block.description}}),t._v(" "),i("div",{ref:"additionalFieldsSection"},t._l(Object.keys(t.selectedBlockView.block.additionalFields),function(e){return i("div",{key:e},[i("div","Operations"==e||"Attributes"==e?[i("h3",{staticClass:"input-title",staticStyle:{"margin-top":"5px","margin-bottom":"5px"}},[t._v("\n          "+t._s(e)+"\n        ")]),t._v(" "),i("ul",{staticClass:"additionalFieldList"},t._l(t.selectedBlockView.block.additionalFields[e],function(n){return i("li",{key:n},[i("div",{staticStyle:{display:"flex","flex-direction":"row","align-items":"center"}},[i("input",{staticClass:"additionalFieldItem",attrs:{id:e},domProps:{value:n}}),t._v(" "),i("button",{staticClass:"deleteAttributeValueBtn",attrs:{role:"button"},on:{click:function(i){return t.deleteItem(e,n)}}},[t._v("\n                X\n              ")])])])}),0),t._v(" "),i("button",{staticClass:"addNewAttributeValueBtn",attrs:{role:"button"},on:{click:function(i){return t.addNewItem(e)}}},[t._v("\n          Add new item\n        ")])]:[i("div",{staticClass:"input-title"},[t._v(t._s(e)+":")]),t._v(" "),i("input",{attrs:{type:"text",placeholder:"Enter property value"},domProps:{value:t.selectedBlockView.block.additionalFields[e]}})])])}),0),t._v(" "),i("button",{staticClass:"btn btn-1",on:{click:function(e){return t.apply(!1)}}},[t._v("\n    Apply Changes\n  ")])])},staticRenderFns:[]};var Q=i("VU/8")(J,K,!1,function(t){i("Wpq5")},"data-v-27bb529c",null).exports,tt=function(){function t(e,i,n,a,o,s){var r=arguments.length>6&&void 0!==arguments[6]?arguments[6]:"Default name "+e,l=arguments.length>7&&void 0!==arguments[7]?arguments[7]:"",c=arguments.length>8&&void 0!==arguments[8]?arguments[8]:null;h()(this,t),this.Id=null,this.Type="",this.coords=[null,null],this.width=null,this.height=null,this.title="",this.description="",this.additionalFields={},this.Id=e,Object.defineProperty(this,"Id",{writable:!1}),this.Type=i,this.coords=[n,a],this.width=o,this.height=s,this.description=l,""===r.replaceAll(" ","")?this.title=i:this.title=r,"Class"===this.Type&&null===c?(this.additionalFields.Attributes=[],this.additionalFields.Operations=[]):this.additionalFields=c}return P()(t,[{key:"setCoords",value:function(t){this.coords=t}},{key:"setWidth",value:function(t){this.width=t}},{key:"setHeight",value:function(t){this.height=t}},{key:"addAttribute",value:function(t){"Class"===this.Type&&this.additionalFields.attrs.push(t)}},{key:"addMethod",value:function(t){"Class"===this.Type&&this.additionalFields.attrs.push(t)}}]),t}(),et=function t(e,i,n,a){h()(this,t),this.Id=null,this.Type="",this.sId=null,this.tId=null,this.Id=e,Object.defineProperty(this,"Id",{writable:!1}),this.Type=i,this.sId=n,this.tId=a},it={name:"DiagramController",components:{DiagramUi:Z,SidePanel:q,EditingPanel:Q},props:{currentDiagram:u},data:function(){return{showDiagramWindow:!1,isLinkAddMode:!1,keyOfDiagramUI:0,selectedBlockView:null}},mounted:function(){this.init()},methods:{init:function(){var t,e=this;(t=this.currentDiagram.Id,console.log("Fetch content of diagram: ",t),g.get("http://127.0.0.1:5000/getDiagramContent",{params:{Id:t}}).then(function(t){return t.data})).then(function(t){t.blocks.forEach(function(t){e.currentDiagram.blocks.push(new tt(t.Id,t.Type,t.coords[0],t.coords[1],t.width,t.height,t.title,t.description,t.additionalFields))}),t.links.forEach(function(t){e.currentDiagram.links.push(new et(t.Id,t.Type,t.sId,t.tId))})}).then(function(){e.showDiagramWindow=!0})},addNewBlock:function(t){var e=this,i={dId:this.currentDiagram.Id,Type:t.Type,coords:[250,250],width:100,height:50,title:t.title};(function(t){return console.log("New block properties: ",t),g.post("http://127.0.0.1:5000/createNewBlock",t).then(function(t){return t.data.bId})})(i).then(function(t){console.log("New block ID:",t);var n=new tt(t,i.Type,i.coords[0],i.coords[1],i.width,i.height,i.title);e.currentDiagram.blocks.push(n),e.$refs.diagramUI.drawNewBlock(n)})},redrawDiagramUI:function(){this.keyOfDiagramUI+=1},toggleLinkMode:function(t){this.isLinkAddMode=t.bool,this.$refs.diagramUI.toggleLinkMode(t)},addNewLink:function(t){var e=this,i=this.$refs.sidePanel.linkType;if(null!=i)if(null!=t.targetID&&null!=t.sourceID){var n={dId:this.currentDiagram.Id,Type:i,sId:t.sourceID,tId:t.targetID};console.log("Creating new link"),function(t){return console.log("New link properties: ",t),g.post("http://127.0.0.1:5000/createNewLink",t).then(function(t){return t.data.lId})}(n).then(function(t){console.log("New Link ID:",t);var i=new et(t,n.Type,n.sId,n.tId);e.currentDiagram.links.push(i),e.$refs.diagramUI.drawNewLink(),e.$refs.sidePanel.clear()})}else console.log("Link creation error: null as ID")},changeSelected:function(t){this.selectedBlockView=t},changeFields:function(t){this.selectedBlockView.block.additionalFields=t.additionalFields,this.selectedBlockView.block.title=t.title,this.selectedBlockView.block.description=t.description,m(this.selectedBlockView.block),this.$refs.diagramUI.changeFields()},updateAdditionalFields:function(t){this.selectedBlockView.block.additionalFields=t,m(this.selectedBlockView.block),this.$refs.diagramUI.changeFields()}},computed:{supportedBlocks:function(){var t=[];return"free"===this.currentDiagram.mode.toLowerCase()?t=["Class","Use-case","Actor"]:"use-case"===this.currentDiagram.Type.toLowerCase()?t=["Use-case","Actor"]:"class"===this.currentDiagram.Type.toLowerCase()?t=["Class"]:console.log("Unsupported schema"),t}}},nt={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticStyle:{display:"flex","flex-direction":"row","margin-top":"20px"}},[t.showDiagramWindow?i("diagram-ui",{key:t.keyOfDiagramUI,ref:"diagramUI",attrs:{currentDiagram:this.currentDiagram},on:{"ready-add-new-link":t.addNewLink,"block-view-selected":t.changeSelected}}):t._e(),t._v(" "),i("div",{staticStyle:{display:"flex","flex-direction":"column"}},[i("side-panel",{ref:"sidePanel",attrs:{"is-link-add-mode":t.isLinkAddMode,"supported-block-types":t.supportedBlocks},on:{"create-block":t.addNewBlock,"toggle-link-mode":t.toggleLinkMode}}),t._v(" "),null!=t.selectedBlockView&&!1===t.isLinkAddMode?i("editing-panel",{attrs:{"selected-block-view":t.selectedBlockView},on:{"close-panel":function(e){t.selectedBlockView=null},"apply-changes":t.changeFields,"item-deleted":t.updateAdditionalFields}}):t._e()],1)],1)},staticRenderFns:[]};var at={name:"App",components:{"diagram-controller":i("VU/8")(it,nt,!1,function(t){i("RT63")},"data-v-00fe1d2e",null).exports},data:function(){return{projects:[],newName:"",newDescription:"",newDiagramType:"Use-case",newDiagramMode:"Free",currentProject:null,currentDiagram:null,showCreateNewProjectDialog:!1,showCreateNewDiagramDialog:!1,state:"project navigator"}},mounted:function(){var t;this.projects=(t=[],g.get("http://127.0.0.1:5000/getProjectList").then(function(e){e.data.forEach(function(e){t.push(new p(e.Id,e.name,e.description))})}),t)},methods:{addProject:function(){var t=this;(function(t){return g.post("http://127.0.0.1:5000/createNewProject",t).then(function(t){return t.data.pId})})({name:this.newName,description:this.newDescription}).then(function(e){console.log("New project ID:",e);var i=new p(e,t.newName,t.newDescription);t.projects=[].concat(o()(t.projects),[i]),t.showCreateNewProjectDialog=!1,t.showProject(i)})},openProject:function(t){var e,i;this.showProject(t),this.currentProject.diagrams=(e=t.Id,i=[],g.get("http://127.0.0.1:5000/getDiagrams",{params:{Id:e}}).then(function(t){t.data.forEach(function(t){i.push(new u(t.Id,t.name,t.description,t.Type,t.mode))})}),i)},showProject:function(t){this.currentProject=t,this.state="diagram navigator",this.newName="",this.newDescription=""},addDiagram:function(){var t=this;(function(t){return console.log("New diagram properties: ",t),g.post("http://127.0.0.1:5000/createNewDiagram",t).then(function(t){return t.data.dId})})({pId:this.currentProject.Id,name:this.newName,description:this.newDescription,Type:this.newDiagramType,mode:this.newDiagramMode}).then(function(e){var i=new u(e,t.newName,t.newDescription,t.newDiagramType,t.newDiagramMode);t.currentProject.diagrams=[].concat(o()(t.currentProject.diagrams),[i]),t.showCreateNewDiagramDialog=!1,t.showDiagram(i)})},openDiagram:function(t){this.showDiagram(t)},showDiagram:function(t){this.currentDiagram=t,this.state="diagram editor",this.newName="",this.newDescription=""},goHome:function(){this.state="project navigator",this.currentDiagram=null,this.currentProject=null},clear:function(){this.newName="",this.newDescription="",this.newDiagramType="use-case",this.newDiagramMode="free"}}},ot={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("div",{staticClass:"navbar"},[i("button",{staticClass:"btn btn-1",on:{click:function(e){return t.goHome()}}},[t._v("\n      Home\n    ")]),t._v(" "),"project navigator"===t.state?i("h1",[t._v("Project navigator")]):"diagram navigator"===t.state?i("h1",[t._v('Project "'+t._s(t.currentProject.name)+'"')]):"diagram editor"===t.state?i("h1",[t._v('Diagram "'+t._s(t.currentDiagram.name)+'"')]):t._e(),t._v(" "),"project navigator"===t.state?i("button",{staticClass:"btn btn-1 btn-sep icon-plus",on:{click:function(e){t.showCreateNewProjectDialog=!0}}},[t._v("\n      Create new project\n    ")]):t._e(),t._v(" "),"diagram navigator"===t.state?i("button",{staticClass:"btn btn-1 btn-sep icon-plus",on:{click:function(e){t.showCreateNewDiagramDialog=!0}}},[t._v("\n      Create new diagram\n    ")]):t._e()]),t._v(" "),"project navigator"===t.state?i("div",{staticClass:"projectTable"},t._l(t.projects,function(e){return i("div",{key:e.Id,staticClass:"column"},[i("div",{staticClass:"card",on:{click:function(i){return t.openProject(e)}}},[i("p",[i("b",[t._v("Name:")]),t._v(" "+t._s(e.name))]),t._v(" "),i("p",[i("b",[t._v("Description:")]),t._v(" "+t._s(e.description))])])])}),0):"diagram navigator"===t.state?i("div",{staticClass:"projectTable"},t._l(t.currentProject.diagrams,function(e){return i("div",{key:e.Id,staticClass:"column"},[i("div",{staticClass:"card",on:{click:function(i){return t.openDiagram(e)}}},[i("p",[i("b",[t._v("Name:")]),t._v(" "+t._s(e.name))]),t._v(" "),i("p",[i("b",[t._v("Description:")]),t._v(" "+t._s(e.description))]),t._v(" "),i("p",[i("b",[t._v("Type:")]),t._v(" "+t._s(e.Type)+" diagram")]),t._v(" "),i("p",[i("b",[t._v("Mode:")]),t._v(" "+t._s(e.mode))])])])}),0):"diagram editor"===t.state?i("div",{staticClass:"diagramEditor"},[i("diagram-controller",{attrs:{"current-diagram":t.currentDiagram}})],1):t._e(),t._v(" "),t.showCreateNewProjectDialog?i("div",{staticClass:"newProjectModal",attrs:{id:"id01"}},[i("form",{staticClass:"newProjectModal-content"},[i("div",{staticClass:"formHeader"},[i("h1",[t._v("Create new project")]),t._v(" "),i("span",{staticClass:"closeForm",attrs:{title:"Close form"},on:{click:function(e){t.showCreateNewProjectDialog=!1}}},[t._v("X")])]),t._v(" "),i("hr"),t._v(" "),i("div",{staticClass:"newProjectForm"},[t._m(0),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.newName,expression:"newName"}],attrs:{id:"NameProj",type:"text",placeholder:"Enter project name",name:"name",required:""},domProps:{value:t.newName},on:{input:function(e){e.target.composing||(t.newName=e.target.value)}}}),t._v(" "),t._m(1),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.newDescription,expression:"newDescription"}],attrs:{id:"DescriptionProj",type:"text",placeholder:"Enter project description",name:"description"},domProps:{value:t.newDescription},on:{input:function(e){e.target.composing||(t.newDescription=e.target.value)}}}),t._v(" "),i("div",{staticClass:"newProjectButtons"},[i("button",{staticClass:"cancelbtn",attrs:{type:"button"},on:{click:function(e){t.showCreateNewProjectDialog=!1}}},[t._v("\n            Cancel\n          ")]),t._v(" "),i("button",{staticClass:"signupbtn",attrs:{type:"button"},on:{click:function(e){return t.addProject()}}},[t._v("Create")])])])])]):t._e(),t._v(" "),t.showCreateNewDiagramDialog?i("div",{staticClass:"newProjectModal"},[i("form",{staticClass:"newProjectModal-content"},[i("div",{staticClass:"formHeader"},[i("h1",[t._v("Create new diagram")]),t._v(" "),i("span",{staticClass:"closeForm",attrs:{title:"Close form"},on:{click:function(e){t.showCreateNewDiagramDialog=!1}}},[t._v("X")])]),t._v(" "),i("hr"),t._v(" "),i("div",{staticClass:"newProjectForm"},[t._m(2),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.newName,expression:"newName"}],attrs:{id:"Name",type:"text",placeholder:"Enter diagram name",name:"name",required:""},domProps:{value:t.newName},on:{input:function(e){e.target.composing||(t.newName=e.target.value)}}}),t._v(" "),t._m(3),t._v(" "),i("input",{directives:[{name:"model",rawName:"v-model",value:t.newDescription,expression:"newDescription"}],attrs:{id:"Description",type:"text",placeholder:"Enter diagram description",name:"description"},domProps:{value:t.newDescription},on:{input:function(e){e.target.composing||(t.newDescription=e.target.value)}}}),t._v(" "),i("div",{staticStyle:{display:"flex","flex-direction":"row","margin-top":"20px"}},[i("div",[t._m(4),t._v(" "),i("select",{directives:[{name:"model",rawName:"v-model",value:t.newDiagramMode,expression:"newDiagramMode"}],on:{change:function(e){var i=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.newDiagramMode=e.target.multiple?i:i[0]}}},[i("option",[t._v("Strict")]),t._v(" "),i("option",[t._v("Free")])])]),t._v(" "),i("div",[t._m(5),t._v(" "),i("select",{directives:[{name:"model",rawName:"v-model",value:t.newDiagramType,expression:"newDiagramType"}],on:{change:function(e){var i=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.newDiagramType=e.target.multiple?i:i[0]}}},[i("option",[t._v("Use-case")]),t._v(" "),i("option",[t._v("Class")])])])]),t._v(" "),i("div",{staticClass:"newProjectButtons"},[i("button",{staticClass:"cancelbtn",attrs:{type:"button"},on:{click:function(e){t.showCreateNewDiagramDialog=!1}}},[t._v("\n            Cancel\n          ")]),t._v(" "),i("button",{staticClass:"signupbtn",attrs:{type:"button"},on:{click:function(e){return t.addDiagram()}}},[t._v("Create")])])])])]):t._e()])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"NameProj"}},[e("b",[this._v("Name")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"DescriptionProj"}},[e("b",[this._v("Description")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"Name"}},[e("b",[this._v("Name")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",{attrs:{for:"Description"}},[e("b",[this._v("Description")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",[e("b",[this._v("Diagram mode")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("label",[e("b",[this._v("Diagram type")])])}]};var st=i("VU/8")(at,ot,!1,function(t){i("fyGi")},null,null).exports,rt=i("/ocq");n.a.use(rt.a);var lt=new rt.a({routes:[]});n.a.config.productionTip=!1,new n.a({el:"#app",router:lt,components:{App:st},template:"<App/>"})},PvSH:function(t,e){},RT63:function(t,e){},Wpq5:function(t,e){},daKz:function(t,e){t.exports="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAiIGhlaWdodD0iODAiIHZpZXdCb3g9IjAgMCA4MCA4MCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzJfMikiPgo8cmVjdCB3aWR0aD0iODAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CjxjaXJjbGUgY3g9IjM5LjUiIGN5PSIxNC41IiByPSIxNC4yNSIgZmlsbD0iIzYwRUZGRiIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLXdpZHRoPSIwLjUiLz4KPGxpbmUgeDE9IjM5LjUiIHkxPSIyOSIgeDI9IjM5LjUiIHkyPSI2MSIgc3Ryb2tlPSJibGFjayIvPgo8bGluZSB4MT0iMzkuMzc0IiB5MT0iNjAuMzEyIiB4Mj0iMjMuMzkwNyIgeTI9IjgwLjMyNjEiIHN0cm9rZT0iYmxhY2siLz4KPGxpbmUgeDE9IjU3LjA5MDMiIHkxPSI3OS45NTMyIiB4Mj0iMzkuNjI2NSIgeTI9IjYwLjMzMjQiIHN0cm9rZT0iYmxhY2siLz4KPGxpbmUgeDE9IjE2IiB5MT0iMzYuNSIgeDI9IjYzIiB5Mj0iMzYuNSIgc3Ryb2tlPSJibGFjayIvPgo8L2c+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzJfMiI+CjxyZWN0IHdpZHRoPSI4MCIgaGVpZ2h0PSI4MCIgZmlsbD0id2hpdGUiLz4KPC9jbGlwUGF0aD4KPC9kZWZzPgo8L3N2Zz4K"},fyGi:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.479c646d44391877b2eb.js.map