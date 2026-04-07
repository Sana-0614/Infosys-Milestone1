import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Heading as RadixThemesHeading,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent} from "$/utils/state"
import {jsx} from "@emotion/react"




function Textfield__root_2f6414eaaf77b7eabb4591a1b7cfb6db () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_04c012f38a1c4e00ffeda9f3d7d23edf = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.infosysproject___infosysproject____search_state.set_search_query", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{onChange:on_change_04c012f38a1c4e00ffeda9f3d7d23edf,placeholder:"Search products..."},)
  )
}


function Grid_bc24f2c12d0e7398d9c633bb70425549 () {
  const reflex___state____state__infosysproject___infosysproject____search_state = useContext(StateContexts.reflex___state____state__infosysproject___infosysproject____search_state)



  return (
    jsx(RadixThemesGrid,{columns:"4",css:({ ["width"] : "100%" }),gap:"4"},Array.prototype.map.call(reflex___state____state__infosysproject___infosysproject____search_state.filtered_products_rx_state_ ?? [],((item_rx_state_,index_9e7dc13d6c7fa41addd66a07442ae2d7)=>(jsx(RadixThemesBox,{css:({ ["border"] : "1px solid gray", ["padding"] : "10px" }),key:index_9e7dc13d6c7fa41addd66a07442ae2d7},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "bold" })},item_rx_state_?.["name"]),jsx(RadixThemesText,{as:"p"},item_rx_state_?.["desc"]))))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesHeading,{},"AI E-Commerce"),jsx(Textfield__root_2f6414eaaf77b7eabb4591a1b7cfb6db,{},),jsx(Grid_bc24f2c12d0e7398d9c633bb70425549,{},)),jsx("title",{},"Infosysproject | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}