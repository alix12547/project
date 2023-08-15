import { useState, useEffect } from 'react'
import { startCreate } from '../api'

const PageContent = () => {

  const [data, setData] = useState({
      proxy_list: [
          '63.143.52.66:92',
          '96.44.151.14:92'
      ],
      type_option: { delay: 100 },
      use_api_phone: false,
      sim_api: { country: 'usa', operator: 'any', product: 'google' },
      browserOptions: { executablePath: undefined, userDataDir: undefined },
      from: 1
  })

  useEffect(() =>{
    
  }, [])

  const loadFile = async e => {
    var input = e.target
    var fReader = new FileReader()
    fReader.readAsDataURL(input.files[0])
    fReader.onloadend = function(event){
        console.log(event.target)
    }
  }
 
  const handleSubmit = async e => {
    e.preventDefault()
    // return console.log('submit', data)
    const resp = await startCreate(data)
    console.log('submit', data, resp)
  }

  return (
    <div className="page-content p-4">
        <div className="d-flex justify-content-between py-2">
          <h5>Gmail Creator</h5>
          <div className="custom-file">
            <input type="file" className="custom-file-input form-control" id="proxy-list-file" />
            <label className="custom-file-label visually-hidden" htmlFor="proxy-list-file">Select proxys list</label>
          </div>
        </div>
        <form className="p-2 mt-5" onSubmit={handleSubmit}>
          <div className="row">
            <div className="col-3">
              <div className="form-group">
                <div className="form-check form-switch">
                  <input className="form-check-input" type="checkbox" id="use-api-check" defaultChecked={data.use_api_phone} onChange={ e => setData({ ...data, use_api_phone:  e.target.checked }) } />
                  <label className="form-check-label" htmlFor="use-api-check">Use 5sim api</label>
                </div>
              </div>
            </div>
            <div className="col-3">
              <div className="form-group mb-4">
                <label htmlFor="country" className="visually-hidden">Country</label>
                <input type="text" className="form-control" id="country" disabled={!data.use_api_phone} placeholder="Country" defaultValue={data.sim_api.country} onChange={ e => setData({ ...data, sim_api: { ...data.sim_api, country: e.target.value } }) } />
              </div>
            </div>
            <div className="col-3">
              <div className="form-group mb-4">
                <label htmlFor="operator" className="visually-hidden">Operator</label>
                <input type="text" className="form-control" id="operator" disabled={!data.use_api_phone} placeholder="Operator" defaultValue={data.sim_api.operator} onChange={ e => setData({ ...data, sim_api: { ...data.sim_api, operator: e.target.value } }) } />
              </div>
            </div>
            <div className="col-3">
              <div className="form-group mb-4">
                <label htmlFor="product" className="visually-hidden">Product</label>
                <input type="text" className="form-control" id="product" disabled={!data.use_api_phone} placeholder="Product" defaultValue={data.sim_api.product} onChange={ e => setData({ ...data, sim_api: { ...data.sim_api, product: e.target.value } }) } />
              </div>
            </div>
          </div>
          <div className="row mb-4">
            <div className="col-6">
              <div className="custom-file">
                <label className="custom-file-label" htmlFor="proxy-list-file">Select Browser</label>
                <input type="file" className="custom-file-input form-control" id="proxy-list-file" onChange={ e => setData({ ...data, browserOptions: { ...data.browserOptions, executablePath: e.target.value } }) } />
              </div>
            </div>
            <div className="col-6">
              <div className="custom-file">
                <label className="custom-file-label" htmlFor="proxy-list-file">Select Profiles Folder</label>
                <input type="file" multiple={false} className="custom-file-input form-control" id="proxy-list-file" />
              </div>
            </div>
          </div>
          <div className="form-group mb-4">
            <label htmlFor="proxy-list" className="visually-hidden">List of proxys</label>
            <textarea className="form-control" id="proxy-list" rows="5" placeholder="List of proxys" defaultValue={data.proxy_list.join('\n')} onChange={ e => setData({ ...data, proxy_list:  e.target.value.trim().split('\n') }) }></textarea>
          </div>
          <div className="row mb-2">
            <div className="col-2">
              <div className="form-group">
                <label htmlFor="option-delay" className="visually-hidden">Option delay ms</label>
                <input type="number" className="form-control" id="option-delay" placeholder="Option delay ms" defaultValue={data.type_option.delay} onChange={ e => setData({ ...data, type_option:  { ...data.type_option, delay: e.target.value } }) } />
              </div>
            </div>
            <div className="col-2">
              <div className="form-group">
                <label htmlFor="option-delay" className="visually-hidden">From</label>
                <input type="number" className="form-control" id="option-delay" placeholder="Option delay ms" defaultValue={data.from} onChange={ e => setData({ ...data, from: e.target.value } ) } />
              </div>
            </div>
            <div className="col-8">
              <div className="form-group">
                <button type="submit" className="btn btn-primary form-control">Start</button>
                </div>
              </div>
          </div>
        </form>
    </div>
  )
}

export default PageContent