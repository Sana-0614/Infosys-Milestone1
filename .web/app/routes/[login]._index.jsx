import {Fragment,useCallback,useContext,useEffect} from "react"
import {Root as RadixFormRoot} from "@radix-ui/react-form"
import {EventLoopContext} from "$/utils/context"
import {ReflexEvent,getRefValue,getRefValues} from "$/utils/state"
import {Button as RadixThemesButton,Flex as RadixThemesFlex,Heading as RadixThemesHeading,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {jsx} from "@emotion/react"




function Root_5ab5ceb8d545ba70da8d3a8414f92347 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

    const handleSubmit_3385a0016a9144946071f3b598abfbf5 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(ReflexEvent("reflex___state____state.infosysproject___infosysproject____login_state.handle_login", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))(ev));

        if (false) {
            $form.reset()
        }
    })
    


  return (
    jsx(RadixFormRoot,{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_3385a0016a9144946071f3b598abfbf5},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesHeading,{},"Login"),jsx(RadixThemesTextField.Root,{name:"email",placeholder:"Email"},),jsx(RadixThemesTextField.Root,{name:"password",type:"password"},),jsx(RadixThemesButton,{type:"submit"},"Login")))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(Root_5ab5ceb8d545ba70da8d3a8414f92347,{},),jsx("title",{},"Infosysproject | Login"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}