webpackJsonp([33],{"16Vf":function(e,t,s){(e.exports=s("FZ+f")(!0)).push([e.i,".disabled-toggle[data-v-18e9c004]{opacity:.5}","",{version:3,sources:["/home/rhf/git/WebAnalysis/src/components/TogglePlotElements.vue"],names:[],mappings:"AACA,kCACE,UAAa,CACd",file:"TogglePlotElements.vue",sourcesContent:["\n.disabled-toggle[data-v-18e9c004] {\n  opacity: 0.5;\n}\n"],sourceRoot:""}])},M9dC:function(e,t,s){"use strict";var a=s("b56K");t.a={name:"TogglePlotElements",mixins:[a.a],props:{isScatterPoints:{type:Boolean,required:!0},isScatterLines:{type:Boolean,required:!0},isErrorBars:{type:Boolean,required:!0},isLegend:{type:Boolean,required:!0},disable:{type:Boolean,required:!0}},computed:{menuItems:function(){return[{text:"Scatter Points",type:"scatterPoint",value:this.isScatterPoints},{text:"Scatter Lines",type:"scatterLine",value:this.isScatterLines},{text:"Error Bars",type:"errorBar",value:this.isErrorBars},{text:"Legend",type:"legend",value:this.isLegend}]}}}},Xaz4:function(e,t,s){"use strict";var a={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("v-menu",{class:{"disabled-toggle":e.disable},attrs:{"offset-y":"",disabled:e.disable}},[s("v-tooltip",{attrs:{slot:"activator",top:""},slot:"activator"},[s("v-btn",{attrs:{slot:"activator",flat:"",small:"",icon:e.isBreakpointSmall},slot:"activator"},[s("span",{staticClass:"hidden-md-and-down"},[e._v("Toggle Elements")]),e._v(" "),s("v-icon",{attrs:{right:!e.isBreakpointSmall}},[e._v("fa-toggle-on")])],1),e._v(" "),s("span",[e._v("Toggle plot elements visibility.")])],1),e._v(" "),s("v-list",e._l(e.menuItems,function(t){return s("v-list-tile",{key:t.text,on:{click:function(s){e.$emit("toggle-plot-element",t.type)}}},[s("v-list-tile-action",[s("v-icon",{attrs:{color:t.value?"success":"error"}},[e._v(e._s(t.value?"fa-check":"fa-times"))])],1),e._v(" "),s("v-list-tile-title",[e._v("\n        "+e._s(t.text)+"\n      ")])],1)}))],1)},staticRenderFns:[]};t.a=a},a1DP:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=s("M9dC"),i=s("Xaz4");var o=function(e){s("lJBW")},n=s("VU/8")(a.a,i.a,!1,o,"data-v-18e9c004",null);t.default=n.exports},lJBW:function(e,t,s){var a=s("16Vf");"string"==typeof a&&(a=[[e.i,a,""]]),a.locals&&(e.exports=a.locals);s("rjj0")("77a12b1e",a,!0,{})}});