webpackJsonp([70],{Fig6:function(r,e,t){"use strict";var o={render:function(){var r=this,e=r.$createElement,t=r._self._c||e;return t("div",[null!==r.vcorrErrorMsg?t("v-flex",{attrs:{xs12:""}},[t("v-alert",{staticClass:"pa-2",attrs:{outline:"",value:!0,type:"warning",transition:"fade-transition",icon:"fa-exclamation-triangle"}},[r._v(r._s(r.vcorrErrorMsg))])],1):r._e(),r._v(" "),null!==r.differentVcorrErrorMsg?t("v-flex",{attrs:{xs12:""}},[t("v-alert",{staticClass:"pa-2",attrs:{outline:"",value:!0,type:"warning",transition:"fade-transition",icon:"fa-exclamation-triangle"}},[r._v(r._s(r.differentVcorrErrorMsg))])],1):r._e(),r._v(" "),t("v-flex",{attrs:{xs12:""}},[t("v-select",{attrs:{items:r.items,"item-text":"name","item-value":"value",label:"VCorr (file to normalize data)",hint:"Select file to Normalize Data",disabled:r.isNormalized},model:{value:r.selected,callback:function(e){r.selected=e},expression:"selected"}})],1)],1)},staticRenderFns:[]};e.a=o},Jd7K:function(r,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=t("l2Cj"),i=t("Fig6"),s=t("VU/8")(o.a,i.a,!1,null,null,null);e.default=s.exports},l2Cj:function(r,e,t){"use strict";var o=t("fZjL"),i=t.n(o),s=t("Dd8w"),n=t.n(s),a=t("NYxO");e.a={name:"VCorrSelect",created:function(){this.setDefaultVCorr()},data:function(){return{m1Error:!1,colltransError:!1,isDifferentVcorr:!1}},computed:n()({},t.i(a.a)("POWDER",{vcorrFiles:function(r){return r.normalizeFilesData.vcorr}}),t.i(a.a)("POWDER/Combine",{normalizeByVCorr:function(r){return r.normalizeByVCorr},selectedData:function(r){return r.selectedData},isNormalized:function(r){return r.isNormalized}}),{vcorrKeys:function(){return i()(this.vcorrFiles)},items:function(){var r=[];for(var e in this.vcorrFiles)r.push({name:e,value:this.vcorrFiles[e]});return r},selected:{get:function(){return this.normalizeByVCorr},set:function(r){this.setNormalizeByVCorr(r)}},vcorrErrorMsg:function(){return this.m1Error&&this.colltransError?"Colltrans is not -80 nor 80 AND M1 is not 9.45 nor 0. Assuming VCorr Ge_115_OUT.":this.m1Error?"M1 is not 9.45 nor 0. Assuming VCorr Ge_115.":this.colltransError?"Colltrans is not -80 nor 80. Assuming VCorr OUT.":null},differentVcorrErrorMsg:function(){return this.isDifferentVcorr?"Atleast one or more files require different VCorr.":null}}),methods:n()({},t.i(a.d)("POWDER/Combine",["setNormalizeByVCorr"]),{resetVcorrErrors:function(){this.m1Error=!1,this.colltransError=!1,this.isDifferentVcorr=!1},vcorrErrors:function(){var r=this,e=[];return this.selectedData.forEach(function(t,o){t.vcorr.colltransError&&(r.isColltransError=!0),t.vcorr.m1Error&&(r.isM1Error=!0),!o||e.indexOf(t.vcorr.filename)>-1?e.push(t.vcorr.filename):r.isDifferentVcorr=!0}),!1},setDefaultVCorr:function(){var r=this.selectedData[0].vcorr.filename;-1!==this.vcorrKeys.indexOf(r)?this.selected=this.vcorrFiles[r]:this.selected=this.vcorrFiles[this.vcorrKeys[0]],this.resetVcorrErrors(),this.vcorrErrors()}}),watch:{selectedData:function(){this.resetVcorrErrors(),this.vcorrErrors()}}}}});