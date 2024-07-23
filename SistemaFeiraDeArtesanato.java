package br.ufpb.dcx.ayla.artesanato;

import java.util.List;

/**
 * Fernando ejh gay
 * Sistema para gerenciar itens de artesanato.
 */
public interface SistemaFeiraDeArtesanato {

    /**
     * Cadastra um novo intem no sistema.
     * @param item O item a ser adicionado
     * @return true se o item foi cadastrado, ou false caso ele já exista no sistema.
     */
    public boolean cadastraItem(ItemDeArtesanato item);

    /**
     * Pesquisa os itens cuja o nome começa com o nome passado como parâmetro
     * @param nome O nome a pesquisar
     * @return uma lista contendo os itens cujos nomes começa com o parâmetro passado
     */
    public List<ItemDeArtesanato> pesquisaItemDeArtesanato(String nome);

    /**
     * Pesquisa os itens abaixo do preço passado
     * @param preco limite para entrar na lista
     * @return uma lista contendo os itens abaixo do preço passado
     */
    public List<ItemDeArtesanato> pesquisaItemAbaixoDoPreco(double preco);

    /**
     * Pesquisa o item cuja o código é passado por parâmetro
     * @param codigo código do item a pesquisar
     * @return o item encontrado
     * @throws ItemInexistenteException se não for encontrado nenhum item com o código passado
     */
    public ItemDeArtesanato pesquisaItemPeloCodigo(String codigo) throws ItemInexistenteException;

}
