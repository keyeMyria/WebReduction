webpackJsonp([53],{J69w:function(e,t,o){"use strict";var s={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-tooltip",{attrs:{top:"","close-delay":1,disabled:e.filesSelected.length<2}},[o("v-btn",{attrs:{slot:"activator",flat:"",small:"",icon:e.isBreakpointSmall,disabled:e.filesSelected.length<2},on:{click:function(t){e.toggle=!e.toggle}},slot:"activator"},[o("span",{staticClass:"hidden-md-and-down"},[e._v(e._s(e.isZoomBrush?"Select":"Zoom"))]),e._v(" "),o("v-icon",{attrs:{right:!e.isBreakpointSmall}},[e._v(e._s(e.isZoomBrush?"crop_free":"zoom_in"))])],1),e._v(" "),o("span",[e._v("Click to enable "+e._s(e.isZoomBrush?"selection":"zoom"))])],1)},staticRenderFns:[]};t.a=s},f7x4:function(e,t,o){var s=o("fdru");"string"==typeof s&&(s=[[e.i,s,""]]),s.locals&&(e.exports=s.locals);o("rjj0")("a0d87fac",s,!0,{})},fdru:function(e,t,o){(e.exports=o("FZ+f")(!0)).push([e.i,"","",{version:3,sources:[],names:[],mappings:"",file:"ToggleZoomBrush.vue",sourceRoot:""}])},hc9F:function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=o("skdi"),i=o("J69w");var n=function(e){o("f7x4")},r=o("VU/8")(s.a,i.a,!1,n,"data-v-5de57de2",null);t.default=r.exports},skdi:function(e,t,o){"use strict";var s=o("Dd8w"),i=o.n(s),n=o("NYxO"),r=o("b56K"),l=o("aCc6");t.a={name:"ToggleZoomBrush",mixins:[r.a],computed:i()({},o.i(n.a)("SANS/Stitch",{isZoomBrush:function(e){return e.isZoomBrush},filesSelected:function(e){return e.filesSelected}}),{toggle:{get:function(){return this.isZoomBrush},set:function(e){if(this.filesSelected.length>1)this.$emit("toggle-edit",e);else{l.a.$emit("add-notification","Need two or more lines to select.","error")}}},label:function(){return this.toggle?"Zoom":"Brush"}}),methods:i()({},o.i(n.d)("SANS/Stitch",["toggleZoomBrush"]))}}});